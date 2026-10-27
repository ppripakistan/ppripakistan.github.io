/**
 * PPRI Community Surveys Flow Engine
 * Handles step-by-step questionnaire, "Other" disclosure, review step,
 * FormSubmit.co background submission, and direct email fallback.
 */

(function () {
  "use strict";

  const FORM_ENDPOINT = "https://formsubmit.co/ajax/ppripakistan@gmail.com";
  const PPRI_EMAIL = "ppripakistan@gmail.com";

  const REGIONS = [
    "Punjab",
    "Sindh",
    "Khyber Pakhtunkhwa",
    "Balochistan",
    "Islamabad Capital Territory",
    "Gilgit-Baltistan",
    "Azad Jammu and Kashmir",
    "Outside Pakistan",
    "Prefer not to say"
  ];

  class SurveyApp {
    constructor(containerEl) {
      this.container = containerEl;
      this.slug = this.container.getAttribute("data-survey-slug");
      this.survey = (window.PPRI_SURVEYS && window.PPRI_SURVEYS[this.slug]) || null;

      if (!this.survey) {
        this.container.innerHTML = `<div class="survey-step-card"><p>Survey configuration not found for slug: ${this.slug}</p></div>`;
        return;
      }

      this.storageKey = `ppri_community_survey_${this.slug}`;
      this.currentStep = 0; // 0 = Intro, 1..5 = Questions, 6 = Review, 7 = Submitting, 8 = Success, 9 = Error
      this.answers = {};
      this.optionalRegion = "";
      this.optionalComments = "";
      this.errorMessage = "";

      this.loadDraft();
      this.render();
    }

    loadDraft() {
      try {
        const raw = sessionStorage.getItem(this.storageKey);
        if (raw) {
          const data = JSON.parse(raw);
          if (data && data.answers) {
            this.answers = data.answers || {};
            this.optionalRegion = data.optionalRegion || "";
            this.optionalComments = data.optionalComments || "";
          }
        }
      } catch (e) {
        console.warn("Could not load survey draft from sessionStorage", e);
      }
    }

    saveDraft() {
      try {
        sessionStorage.setItem(
          this.storageKey,
          JSON.stringify({
            answers: this.answers,
            optionalRegion: this.optionalRegion,
            optionalComments: this.optionalComments,
            timestamp: new Date().toISOString()
          })
        );
      } catch (e) {
        console.warn("Could not save survey draft to sessionStorage", e);
      }
    }

    clearDraft() {
      try {
        sessionStorage.removeItem(this.storageKey);
      } catch (e) {
        console.warn("Could not clear survey draft", e);
      }
    }

    goToStep(step) {
      this.currentStep = step;
      this.render();
      this.container.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    setAnswer(qId, option, otherText = "") {
      this.answers[qId] = {
        option: option,
        otherText: otherText
      };
      this.saveDraft();
    }

    getAnswer(qId) {
      return this.answers[qId] || null;
    }

    render() {
      if (this.currentStep === 0) {
        this.renderIntro();
      } else if (this.currentStep >= 1 && this.currentStep <= 5) {
        this.renderQuestion(this.currentStep);
      } else if (this.currentStep === 6) {
        this.renderReview();
      } else if (this.currentStep === 7) {
        this.renderSubmitting();
      } else if (this.currentStep === 8) {
        this.renderSuccess();
      } else if (this.currentStep === 9) {
        this.renderError();
      }
    }

    /* -------------------------------------------------------------
       STEP 0: INTRO SCREEN
       ------------------------------------------------------------- */
    renderIntro() {
      this.container.innerHTML = `
        <div class="survey-step-card survey-intro-box">
          <div class="survey-intro-icon">
            ${this.survey.icon}
          </div>
          <h1>${this.survey.title}</h1>
          <p class="desc">${this.survey.detailedDescription || this.survey.shortDescription}</p>
          
          <div class="survey-intro-badges">
            <span class="survey-intro-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              ${this.survey.time}
            </span>
            <span class="survey-intro-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              5 simple questions
            </span>
            <span class="survey-intro-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              No account required
            </span>
          </div>

          <div>
            <button type="button" class="survey-intro-btn" id="btnStartSurvey">
              Start survey &rarr;
            </button>
          </div>
        </div>
      `;

      const startBtn = this.container.querySelector("#btnStartSurvey");
      if (startBtn) {
        startBtn.addEventListener("click", () => this.goToStep(1));
      }
    }

    /* -------------------------------------------------------------
       STEPS 1..5: SINGLE QUESTION FLOW
       ------------------------------------------------------------- */
    renderQuestion(qIndex) {
      const qData = this.survey.questions[qIndex - 1];
      const existing = this.getAnswer(qData.id);
      const isSelected = !!existing;
      const progressPercent = Math.round((qIndex / 5) * 100);

      let optionsHtml = "";
      qData.options.forEach((optText, optIdx) => {
        const isOther = optText.toLowerCase().includes("other");
        const checked = existing && existing.option === optText;
        const otherVal = checked && existing.otherText ? existing.otherText : "";

        optionsHtml += `
          <div>
            <label class="survey-option-label ${checked ? "is-selected" : ""}" data-opt-index="${optIdx}">
              <input 
                type="radio" 
                name="${qData.id}" 
                value="${optText}" 
                class="survey-option-input" 
                ${checked ? "checked" : ""}
              />
              <span class="survey-option-text">${optText}</span>
            </label>
            ${
              isOther
                ? `
                <div class="survey-other-disclosure ${checked ? "is-visible" : ""}" id="otherDisclosure_${qData.id}">
                  <label class="survey-other-label" for="otherInput_${qData.id}">Please tell us more (optional):</label>
                  <input 
                    type="text" 
                    id="otherInput_${qData.id}" 
                    class="survey-other-input" 
                    placeholder="Type your answer here..." 
                    maxlength="250" 
                    value="${otherVal.replace(/"/g, "&quot;")}"
                  />
                  <div class="survey-other-meta">
                    <span id="charCount_${qData.id}">${otherVal.length} / 250</span>
                  </div>
                </div>
              `
                : ""
            }
          </div>
        `;
      });

      const isLast = qIndex === 5;
      const nextBtnLabel = isLast ? "Review answers &rarr;" : "Next question &rarr;";

      this.container.innerHTML = `
        <div class="survey-flow-header">
          <div class="survey-flow-progress-meta">
            <span class="step-count">Question ${qIndex} of 5</span>
            <span class="progress-pct">${progressPercent}% completed</span>
          </div>
          <div class="survey-progress-bar" role="progressbar" aria-valuenow="${progressPercent}" aria-valuemin="0" aria-valuemax="100">
            <div class="survey-progress-fill" style="width: ${progressPercent}%;"></div>
          </div>
        </div>

        <div class="survey-step-card">
          <div class="survey-question-prompt">
            <h2>${qIndex}. ${qData.text}</h2>
            <p class="hint">Select the option that best describes your view.</p>
          </div>

          <form id="questionForm" onsubmit="return false;">
            <div class="survey-options-list">
              ${optionsHtml}
            </div>

            <div class="survey-nav-actions">
              ${
                qIndex > 1
                  ? `<button type="button" class="survey-btn survey-btn-secondary" id="btnBack">&larr; Back</button>`
                  : `<div></div>`
              }
              <button 
                type="button" 
                class="survey-btn survey-btn-primary" 
                id="btnNext" 
                ${!isSelected ? "disabled" : ""}
              >
                ${nextBtnLabel}
              </button>
            </div>
          </form>
        </div>
      `;

      // Event Listeners for Radio Options
      const nextBtn = this.container.querySelector("#btnNext");
      const backBtn = this.container.querySelector("#btnBack");
      const labels = this.container.querySelectorAll(".survey-option-label");
      const otherDisclosure = this.container.querySelector(`#otherDisclosure_${qData.id}`);
      const otherInput = this.container.querySelector(`#otherInput_${qData.id}`);
      const charCount = this.container.querySelector(`#charCount_${qData.id}`);

      labels.forEach((lbl) => {
        const input = lbl.querySelector("input[type='radio']");
        input.addEventListener("change", () => {
          labels.forEach((l) => l.classList.remove("is-selected"));
          lbl.classList.add("is-selected");

          const optVal = input.value;
          const isOther = optVal.toLowerCase().includes("other");

          if (isOther && otherDisclosure) {
            otherDisclosure.classList.add("is-visible");
            const txt = otherInput ? otherInput.value.trim() : "";
            this.setAnswer(qData.id, optVal, txt);
            if (otherInput) otherInput.focus();
          } else {
            if (otherDisclosure) {
              otherDisclosure.classList.remove("is-visible");
              if (otherInput) otherInput.value = "";
              if (charCount) charCount.textContent = "0 / 250";
            }
            this.setAnswer(qData.id, optVal, "");
          }

          if (nextBtn) nextBtn.disabled = false;
        });
      });

      if (otherInput) {
        otherInput.addEventListener("input", (e) => {
          const val = e.target.value;
          if (charCount) charCount.textContent = `${val.length} / 250`;
          const currentAns = this.getAnswer(qData.id);
          if (currentAns) {
            this.setAnswer(qData.id, currentAns.option, val);
          }
        });
      }

      if (backBtn) {
        backBtn.addEventListener("click", () => this.goToStep(qIndex - 1));
      }

      if (nextBtn) {
        nextBtn.addEventListener("click", () => {
          if (!this.getAnswer(qData.id)) return;
          this.goToStep(qIndex + 1);
        });
      }
    }

    /* -------------------------------------------------------------
       STEP 6: REVIEW SCREEN
       ------------------------------------------------------------- */
    renderReview() {
      let itemsHtml = "";
      this.survey.questions.forEach((q, idx) => {
        const ans = this.getAnswer(q.id);
        let displayAns = ans ? ans.option : "<em>Not answered</em>";
        if (ans && ans.otherText) {
          displayAns += ` <span style="color: #1b5e39; font-weight: 600;">("${ans.otherText}")</span>`;
        }

        itemsHtml += `
          <div class="survey-review-item">
            <div class="survey-review-content">
              <div class="survey-review-question">Question ${idx + 1}. ${q.text}</div>
              <div class="survey-review-answer">${displayAns}</div>
            </div>
            <button type="button" class="survey-review-edit-btn" data-goto-q="${idx + 1}" aria-label="Edit question ${idx + 1}">
              Edit
            </button>
          </div>
        `;
      });

      let regionOptionsHtml = `<option value="">Select your region or province (optional)</option>`;
      REGIONS.forEach((r) => {
        const selected = this.optionalRegion === r ? "selected" : "";
        regionOptionsHtml += `<option value="${r}" ${selected}>${r}</option>`;
      });

      this.container.innerHTML = `
        <div class="survey-step-card">
          <div class="survey-review-header">
            <h2>Review your answers</h2>
            <p>Please check your responses below before submitting. You can edit any answer or add optional thoughts.</p>
          </div>

          <div class="survey-review-list">
            ${itemsHtml}
          </div>

          <div class="survey-optional-section">
            <div class="survey-field-group">
              <label for="reviewRegion">
                Province or region <span class="field-hint">(optional — helps regional research)</span>
              </label>
              <select id="reviewRegion">
                ${regionOptionsHtml}
              </select>
            </div>

            <div class="survey-field-group">
              <label for="reviewComments">
                Anything else you would like to share? <span class="field-hint">(optional)</span>
              </label>
              <textarea 
                id="reviewComments" 
                rows="3" 
                placeholder="Share any additional thoughts here..." 
                maxlength="1000"
              >${this.optionalComments}</textarea>
            </div>
          </div>

          <div class="survey-nav-actions" style="margin-top: 28px;">
            <button type="button" class="survey-btn survey-btn-secondary" id="btnBackToQ5">
              &larr; Back to questions
            </button>
            <button type="button" class="survey-btn survey-btn-primary" id="btnSubmitSurvey">
              Submit survey ✓
            </button>
          </div>
        </div>
      `;

      // Event Listeners
      const editBtns = this.container.querySelectorAll(".survey-review-edit-btn");
      editBtns.forEach((btn) => {
        btn.addEventListener("click", () => {
          const targetQ = parseInt(btn.getAttribute("data-goto-q"), 10);
          this.goToStep(targetQ);
        });
      });

      const regionSelect = this.container.querySelector("#reviewRegion");
      if (regionSelect) {
        regionSelect.addEventListener("change", (e) => {
          this.optionalRegion = e.target.value;
          this.saveDraft();
        });
      }

      const commentsText = this.container.querySelector("#reviewComments");
      if (commentsText) {
        commentsText.addEventListener("input", (e) => {
          this.optionalComments = e.target.value;
          this.saveDraft();
        });
      }

      const backToQ5 = this.container.querySelector("#btnBackToQ5");
      if (backToQ5) {
        backToQ5.addEventListener("click", () => this.goToStep(5));
      }

      const submitBtn = this.container.querySelector("#btnSubmitSurvey");
      if (submitBtn) {
        submitBtn.addEventListener("click", () => this.handleSubmission());
      }
    }

    /* -------------------------------------------------------------
       STEP 7: SUBMITTING STATE
       ------------------------------------------------------------- */
    renderSubmitting() {
      this.container.innerHTML = `
        <div class="survey-step-card survey-status-box">
          <div class="survey-spinner"></div>
          <h2>Submitting your response...</h2>
          <p>Please wait a moment while we send your answers to PPRI researchers.</p>
        </div>
      `;
    }

    /* -------------------------------------------------------------
       STEP 8: SUCCESS CONFIRMATION
       ------------------------------------------------------------- */
    renderSuccess() {
      this.container.innerHTML = `
        <div class="survey-step-card survey-status-box">
          <div class="survey-success-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
          </div>
          <h2>Thank you for sharing your views!</h2>
          <p>Your response has been submitted. Your feedback will help PPRI researchers better understand the issues people face.</p>
          <div class="survey-success-actions">
            <a href="/surveys/" class="survey-btn survey-btn-primary">Back to all surveys</a>
            <a href="/research/" class="survey-btn survey-btn-secondary">Explore PPRI research</a>
          </div>
        </div>
      `;
    }

    /* -------------------------------------------------------------
       STEP 9: ERROR STATE & RETRY
       ------------------------------------------------------------- */
    renderError() {
      const emailDraft = this.buildEmailDraft();
      const subject = this.buildEmailSubject();
      const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(PPRI_EMAIL)}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailDraft)}`;
      const mailtoUrl = `mailto:${encodeURIComponent(PPRI_EMAIL)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailDraft)}`;

      this.container.innerHTML = `
        <div class="survey-step-card">
          <div class="survey-error-alert">
            <h4>Connection or submission issue</h4>
            <p>${this.errorMessage || "Unable to reach the submission service. Your responses have been kept safe."}</p>
            <div class="survey-error-actions">
              <button type="button" class="survey-btn survey-btn-primary" id="btnRetrySubmit">
                Try again
              </button>
              <a href="${gmailUrl}" target="_blank" rel="noopener" class="survey-btn survey-btn-secondary">
                Submit via Gmail
              </a>
              <a href="${mailtoUrl}" class="survey-btn survey-btn-secondary">
                Submit via Email app
              </a>
            </div>
          </div>

          <div style="margin-top: 24px; text-align: center;">
            <button type="button" class="survey-btn survey-btn-secondary" id="btnBackToReview">
              &larr; Return to review answers
            </button>
          </div>
        </div>
      `;

      const retryBtn = this.container.querySelector("#btnRetrySubmit");
      if (retryBtn) {
        retryBtn.addEventListener("click", () => this.handleSubmission());
      }

      const backBtn = this.container.querySelector("#btnBackToReview");
      if (backBtn) {
        backBtn.addEventListener("click", () => this.goToStep(6));
      }
    }

    /* -------------------------------------------------------------
       EMAIL & DATA PAYLOAD BUILDERS
       ------------------------------------------------------------- */
    buildEmailSubject() {
      const regionPart = this.optionalRegion ? ` - ${this.optionalRegion}` : " - General";
      return `[PPRI-SURVEY: ${this.slug.toUpperCase()}] ${this.survey.title}${regionPart}`;
    }

    buildEmailDraft() {
      let text = `PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI)\n`;
      text += `COMMUNITY SURVEY SUBMISSION\n`;
      text += `==================================================\n`;
      text += `SURVEY: ${this.survey.title} (#${this.survey.number})\n`;
      text += `SURVEY SLUG: ${this.slug}\n`;
      text += `REGION: ${this.optionalRegion || "Not specified"}\n`;
      text += `TIMESTAMP: ${new Date().toLocaleString("en-PK", { timeZone: "Asia/Karachi" })} (PKT)\n`;
      text += `ORIGIN: ${window.location.href}\n`;
      text += `==================================================\n\n`;

      this.survey.questions.forEach((q, idx) => {
        const ans = this.getAnswer(q.id);
        const opt = ans ? ans.option : "Not answered";
        const extra = ans && ans.otherText ? ` [Details: ${ans.otherText}]` : "";
        text += `Question ${idx + 1}: ${q.text}\n`;
        text += `Response: ${opt}${extra}\n\n`;
      });

      text += `--------------------------------------------------\n`;
      text += `ADDITIONAL COMMENTS:\n`;
      text += `${this.optionalComments.trim() ? this.optionalComments.trim() : "None provided"}\n\n`;
      text += `--------------------------------------------------\n`;
      text += `Submitted via PPRI Community Surveys Portal\n`;

      return text;
    }

    async handleSubmission() {
      this.goToStep(7); // Show Submitting state

      const emailSubject = this.buildEmailSubject();
      const emailBody = this.buildEmailDraft();

      const payload = {
        _subject: emailSubject,
        _template: "table",
        _captcha: "false",
        survey_title: this.survey.title,
        survey_slug: this.slug,
        region: this.optionalRegion || "Not specified",
        comments: this.optionalComments || "None provided",
        full_transcript: emailBody
      };

      // Add each question and answer as explicit fields for FormSubmit table view
      this.survey.questions.forEach((q, idx) => {
        const ans = this.getAnswer(q.id);
        let val = ans ? ans.option : "Not answered";
        if (ans && ans.otherText) {
          val += ` (Other: ${ans.otherText})`;
        }
        payload[`q${idx + 1}_${q.id}`] = `${q.text}: ${val}`;
      });

      try {
        const res = await fetch(FORM_ENDPOINT, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json"
          },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          this.clearDraft();
          this.goToStep(8); // Success
        } else {
          const errData = await res.json().catch(() => ({}));
          this.errorMessage = errData.message || `Server responded with status ${res.status}.`;
          this.goToStep(9); // Error
        }
      } catch (err) {
        console.error("Submission fetch error:", err);
        this.errorMessage = "Network connection failed or service was unreachable.";
        this.goToStep(9); // Error
      }
    }
  }

  // Auto-initialize when DOM is ready
  document.addEventListener("DOMContentLoaded", function () {
    const containers = document.querySelectorAll("[data-survey-engine]");
    containers.forEach((el) => new SurveyApp(el));
  });
})();
