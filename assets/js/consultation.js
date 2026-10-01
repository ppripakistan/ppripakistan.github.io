document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("[data-idea-form]");
  const preview = document.querySelector("[data-submission-preview]");
  const status = document.querySelector("[data-submission-status]");
  const copyButton = document.querySelector("[data-copy-submission]");
  const clearButton = document.querySelector("[data-clear-submission]");
  if (!form || !preview || !status) return;

  const submissionAddress = "ppripakistan@gmail.com";
  let lastDraft = "";

  const buildDraft = () => {
    const data = new FormData(form);
    const name = String(data.get("name") || "Not provided").trim();
    const email = String(data.get("email") || "Not provided").trim();
    const category = String(data.get("category") || "Other reform idea").trim();
    const title = String(data.get("title") || "Untitled idea").trim();
    const location = String(data.get("location") || "Not provided").trim();
    const idea = String(data.get("idea") || "").trim();
    const evidence = String(data.get("evidence") || "Not provided").trim();

    return [
      "PPRI PUBLIC IDEA SUBMISSION",
      "============================",
      `Title: ${title}`,
      `Category: ${category}`,
      `Name: ${name}`,
      `Email: ${email}`,
      `Location / area (optional): ${location}`,
      "",
      "Idea / question:",
      idea,
      "",
      "Evidence / references (optional):",
      evidence,
      "",
      `Prepared from: ${window.location.origin}${window.location.pathname}`,
    ].join("\n");
  };

  const openGmail = (draft) => {
    const data = new FormData(form);
    const title = String(data.get("title") || "PPRI research idea").trim();
    const subject = `PPRI Research Idea — ${title}`;
    const gmailUrl = new URL("https://mail.google.com/mail/");
    gmailUrl.searchParams.set("view", "cm");
    gmailUrl.searchParams.set("fs", "1");
    gmailUrl.searchParams.set("to", submissionAddress);
    gmailUrl.searchParams.set("su", subject);
    gmailUrl.searchParams.set("body", draft);

    const popup = window.open(gmailUrl.toString(), "_blank", "noopener,noreferrer");
    if (popup) {
      status.textContent = `Gmail was opened with your submission addressed to ${submissionAddress}. Review it and press Send when you are ready.`;
    } else {
      status.innerHTML = `Your browser blocked the Gmail window. <a href="${gmailUrl.toString()}" target="_blank" rel="noopener">Open Gmail manually</a> and review the prepared submission.`;
    }
  };

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    lastDraft = buildDraft();
    preview.textContent = lastDraft;
    preview.classList.add("is-visible");
    openGmail(lastDraft);
  });

  copyButton?.addEventListener("click", async () => {
    if (!lastDraft) {
      lastDraft = buildDraft();
      preview.textContent = lastDraft;
      preview.classList.add("is-visible");
    }
    try {
      await navigator.clipboard.writeText(lastDraft);
      status.textContent = "Submission copied to your clipboard.";
    } catch {
      status.textContent = "Clipboard access is unavailable in this browser. Select the draft below and copy it manually.";
    }
  });

  clearButton?.addEventListener("click", () => {
    form.reset();
    lastDraft = "";
    preview.textContent = "";
    preview.classList.remove("is-visible");
    status.textContent = "Nothing has been sent. Fill the form and use the Gmail button when you are ready.";
  });
});
