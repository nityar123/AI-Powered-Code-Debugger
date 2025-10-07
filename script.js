async function debugCode() {
  const code = document.getElementById("code").value;
  const language = document.getElementById("language").value;
  const output = document.getElementById("output");

  output.textContent = "Analyzing code...";

  const response = await fetch("/debug", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code, language })
  });

  const data = await response.json();
  output.textContent = data.suggestion || data.error;
}
