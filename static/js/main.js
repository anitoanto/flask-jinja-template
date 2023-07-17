function loaderTesting() {
  let loader = document.getElementById("loader");
  console.log(loader);
  showElement(loader);
  setTimeout(() => {
    hideElement(loader);
  }, 2000);
}

function showElement(element) {
  element.classList.remove("hidden");
  element.classList.add("show");
}

function hideElement(element) {
  element.classList.remove("show");
  element.classList.add("hidden");
}
