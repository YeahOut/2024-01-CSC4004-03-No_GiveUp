function changeWorkBreak(e) {
    const container = document.querySelector('.report_main_container');
    container.style.wordBreak = e.target.value;
}

function setReportText() {
  const element = document.getElementById("report_paragraph_container");
  element.innerHTML
    = "<p>asdadasadadasdsdsdsd</p>";
} 