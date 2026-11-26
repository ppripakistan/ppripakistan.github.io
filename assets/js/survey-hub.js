/**
 * PPRI Thematic Consultation Survey Hub
 * Frictionless Gmail & Default Email Client Integration
 */
document.addEventListener("DOMContentLoaded", function () {
  "use strict";

  // --- TOPIC TAB SWITCHER ---
  const topicBtns = Array.from(document.querySelectorAll(".survey-topic-btn"));
  const topicPanes = document.querySelectorAll(".survey-topic-pane");

  function activateTopic(targetBtn, moveFocus) {
    const topicId = targetBtn.getAttribute("data-topic");
    topicBtns.forEach((b) => {
      const isSelected = b === targetBtn;
      b.classList.toggle("active", isSelected);
      b.setAttribute("aria-selected", isSelected ? "true" : "false");
      b.setAttribute("tabindex", isSelected ? "0" : "-1");
    });
    topicPanes.forEach((p) => {
      const isActive = p.id === topicId;
      p.classList.toggle("active", isActive);
      p.hidden = !isActive;
    });
    if (moveFocus) targetBtn.focus();
  }

  topicBtns.forEach(function (btn, idx) {
    if (!btn.hasAttribute("tabindex")) {
      btn.setAttribute("tabindex", btn.classList.contains("active") ? "0" : "-1");
    }
    btn.addEventListener("click", function () {
      activateTopic(this, false);
    });
    btn.addEventListener("keydown", function (e) {
      const isRtl = getComputedStyle(this.parentElement || document.documentElement).direction === "rtl";
      let nextIdx = null;
      if (e.key === "ArrowRight") nextIdx = isRtl ? (idx - 1 + topicBtns.length) % topicBtns.length : (idx + 1) % topicBtns.length;
      else if (e.key === "ArrowLeft") nextIdx = isRtl ? (idx + 1) % topicBtns.length : (idx - 1 + topicBtns.length) % topicBtns.length;
      else if (e.key === "Home") nextIdx = 0;
      else if (e.key === "End") nextIdx = topicBtns.length - 1;
      if (nextIdx !== null) {
        e.preventDefault();
        activateTopic(topicBtns[nextIdx], true);
      }
    });
  });

  // --- SCALE BUTTON INTERACTION ---
  document.querySelectorAll(".survey-scale").forEach(function (scaleGroup) {
    const btns = scaleGroup.querySelectorAll(".scale-btn");
    btns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        btns.forEach((b) => b.classList.remove("is-selected"));
        this.classList.add("is-selected");
        const input = this.querySelector("input[type='radio']");
        if (input) input.checked = true;
      });
    });
  });

  // --- SUBMISSION LOGIC ---
  const modal = document.getElementById("submissionModal");
  const modalSummaryText = document.getElementById("modalSummaryText");
  const btnGmail = document.getElementById("btnSendGmail");
  const btnEmail = document.getElementById("btnSendEmail");
  const btnCopy = document.getElementById("btnCopySurvey");
  const btnCloseModal = document.getElementById("btnCloseSubmissionModal");
  let lastFocusedEl = null;

  function setBackgroundInert(isInert) {
    const header = document.querySelector(".site-header");
    const footer = document.querySelector(".site-footer");
    if (header) header.inert = isInert;
    if (footer) footer.inert = isInert;
    const main = document.getElementById("main-content");
    if (main) {
      Array.from(main.children).forEach(function (child) {
        if (child !== modal) child.inert = isInert;
      });
    }
  }

  function closeSubmissionModal() {
    if (!modal) return;
    modal.classList.remove("active");
    modal.hidden = true;
    setBackgroundInert(false);
    if (lastFocusedEl && typeof lastFocusedEl.focus === "function") {
      lastFocusedEl.focus();
      lastFocusedEl = null;
    }
  }

  if (btnCloseModal) {
    btnCloseModal.addEventListener("click", closeSubmissionModal);
  }
  if (modal) {
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeSubmissionModal();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !modal.hidden && modal.classList.contains("active")) {
        e.preventDefault();
        closeSubmissionModal();
      }
    });
  }

  let currentSubmissionText = "";
  let currentTopicTitle = "";

  window.handleSurveySubmit = function (formId, topicTitle) {
    const form = document.getElementById(formId);
    if (!form) return;

    lastFocusedEl = document.activeElement;
    const formData = new FormData(form);
    const answers = [];
    currentTopicTitle = topicTitle;

    // Collect elements and their labels
    const questions = form.querySelectorAll(".survey-question");
    questions.forEach(function (qEl, idx) {
      const qTitleEl = qEl.querySelector("h3");
      const qText = qTitleEl ? qTitleEl.textContent.trim() : `Question ${idx + 1}`;
      
      const inputs = qEl.querySelectorAll("input:checked, select, textarea");
      const vals = [];
      inputs.forEach(function (inp) {
        if (inp.type === "radio" || inp.type === "checkbox") {
          if (inp.checked && inp.value) vals.push(inp.value);
        } else if (inp.value && inp.value.trim() !== "") {
          vals.push(inp.value.trim());
        }
      });

      const answerText = vals.length > 0 ? vals.join("; ") : "Not answered";
      answers.push({ question: qText, answer: answerText });
    });

    // Respondent Region
    const regionSelect = form.querySelector("select[name^='respondent_region']");
    const regionVal = (regionSelect && regionSelect.value) || formData.get("respondent_region") || "General Citizen";
    const commentsVal = formData.get("comments") || "None";

    // Build plain text for email
    let emailBody = `PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI)\n`;
    emailBody += `PUBLIC CONSULTATION SUBMISSION\n`;
    emailBody += `--------------------------------------------------\n`;
    emailBody += `TOPIC: ${topicTitle}\n`;
    emailBody += `REGION: ${regionVal}\n`;
    emailBody += `DATE: ${new Date().toLocaleDateString("en-PK")}\n`;
    emailBody += `--------------------------------------------------\n\n`;

    answers.forEach(function (item, i) {
      emailBody += `Q${i + 1}: ${item.question}\n`;
      emailBody += `Response: ${item.answer}\n\n`;
    });

    if (commentsVal && commentsVal !== "None") {
      emailBody += `Additional Comments:\n${commentsVal}\n\n`;
    }

    emailBody += `--------------------------------------------------\n`;
    emailBody += `Submitted via PPRI Interactive Consultation Hub\n`;
    emailBody += `https://ppripakistan.github.io/surveys/`;

    currentSubmissionText = emailBody;

    // Save locally
    const storageKey = `ppri_survey_${formId}`;
    localStorage.setItem(storageKey, JSON.stringify({
      topic: topicTitle,
      body: emailBody,
      timestamp: new Date().toISOString()
    }));

    // Update Modal
    if (modalSummaryText) {
      modalSummaryText.textContent = emailBody;
    }

    // Configure Direct Gmail Web Compose link
    const emailTo = "ppripakistan@gmail.com";
    const subject = `[PPRI Consultation] Submission: ${topicTitle} - ${regionVal}`;
    const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(emailTo)}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
    const mailtoUrl = `mailto:${encodeURIComponent(emailTo)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;

    if (btnGmail) {
      btnGmail.setAttribute("href", gmailUrl);
      btnGmail.setAttribute("target", "_blank");
      btnGmail.setAttribute("rel", "noopener noreferrer");
    }
    if (btnEmail) {
      btnEmail.setAttribute("href", mailtoUrl);
    }

    if (modal) {
      modal.hidden = false;
      modal.classList.add("active");
      setBackgroundInert(true);
      const focusTarget = btnGmail || btnCloseModal || modal;
      if (focusTarget && typeof focusTarget.focus === "function") {
        focusTarget.focus();
      }
    }
  };

  // Copy Answers Button
  if (btnCopy) {
    btnCopy.addEventListener("click", function () {
      if (!currentSubmissionText) return;
      navigator.clipboard.writeText(currentSubmissionText).then(function () {
        const origText = btnCopy.textContent;
        btnCopy.textContent = "Copied to Clipboard! ✓";
        setTimeout(() => { btnCopy.textContent = origText; }, 2500);
      }).catch(function () {
        alert("Unable to auto-copy. Please select and copy the text box directly.");
      });
    });
  }
});
