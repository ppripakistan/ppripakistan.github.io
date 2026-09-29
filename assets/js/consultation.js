document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("[data-idea-form]");
  const preview = document.querySelector("[data-submission-preview]");
  const status = document.querySelector("[data-submission-status]");
  const copyButton = document.querySelector("[data-copy-submission]");
  const clearButton = document.querySelector("[data-clear-submission]");
  if (!form || !preview || !status) return;

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

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    lastDraft = buildDraft();
    preview.textContent = lastDraft;
    preview.classList.add("is-visible");
    status.textContent = "Your submission draft is ready. Copy it for your records or save it locally. An official online submission endpoint is not connected to this static site yet.";
    status.setAttribute("role", "status");
    copyButton?.focus();
  });

  copyButton?.addEventListener("click", async () => {
    if (!lastDraft) return;
    try {
      await navigator.clipboard.writeText(lastDraft);
      status.textContent = "Submission draft copied to your clipboard.";
    } catch {
      status.textContent = "Clipboard access is unavailable in this browser. Select the draft below and copy it manually.";
    }
  });

  clearButton?.addEventListener("click", () => {
    form.reset();
    lastDraft = "";
    preview.textContent = "";
    preview.classList.remove("is-visible");
    status.textContent = "Nothing has been submitted. This page only prepares a structured draft until an official submission channel is connected.";
  });
});
