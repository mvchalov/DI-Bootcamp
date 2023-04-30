addEventListener("DOMContentLoaded", (event) => {
  if (document.querySelectorAll("form").length > 0) {
    document.querySelectorAll("form input").forEach((e) => {
      if (!e.classList.contains("form-control")) {
        e.classList.add("form-control");
      }
    });
    document.querySelectorAll("form label").forEach((e) => {
      if (!e.classList.contains("form-control")) {
        e.classList.add("form-label");
        e.classList.add("pt-3");
      }
    });
    document.querySelectorAll("form select").forEach((e) => {
      if (!e.classList.contains("form-control")) {
        e.classList.add("form-select");
      }
    });
  }
});
