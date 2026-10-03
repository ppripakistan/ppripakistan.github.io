/**
 * PPRI Thematic Consultation Survey Hub
 * Frictionless Gmail & Default Email Client Integration
 */
document.addEventListener("DOMContentLoaded", function () {
  "use strict";

  // --- TOPIC TAB SWITCHER ---
  const topicBtns = document.querySelectorAll(".survey-topic-btn");
  const topicPanes = document.querySelectorAll(".survey-topic-pane");

  topicBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const topicId = this.getAttribute("data-topic");
      topicBtns.forEach((b) => b.classList.remove("active"));
      topicPanes.forEach((p) => p.classList.remove("active"));
      this.classList.add("active");
      const activePane = document.getElementById(topicId);
      if (activePane) activePane.classList.add("active");
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

  let currentSubmissionText = "";
  let currentTopicTitle = "";

  window.handleSurveySubmit = function (formId, topicTitle) {
    const form = document.getElementById(formId);
    if (!form) return;

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
    const regionVal = formData.get("respondent_region") || "General Citizen";
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
    emailBody += `https://ppripakistan.github.io/consultation/survey.html`;

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
    const emailTo = "consultation@ppri.org.pk";
    const subject = `[PPRI Consultation] Submission: ${topicTitle} - ${regionVal}`;
    const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(emailTo)}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
    const mailtoUrl = `mailto:${encodeURIComponent(emailTo)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;

    if (btnGmail) {
      btnGmail.href = gmailUrl;
      btnGmail.target = "_blank";
    }
    if (btnEmail) {
      btnEmail.href = mailtoUrl;
    }

    if (modal) {
      modal.classList.add("active");
      modal.scrollIntoView({ behavior: "smooth" });
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
