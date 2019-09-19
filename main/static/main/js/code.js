// Show Project
const projectsList = document.querySelectorAll(".project");

const showProject = () => {
  let time = 0;
  for (const project of projectsList) {
    if (project.offsetTop < (window.scrollY + window.innerHeight / 1.3)) {
      setTimeout(function () {
        project.classList.add("show-project");
      }, time
      )
    }
    time += 60;
  }
}

showProject();
document.addEventListener("scroll", showProject);

// Show Authors

const authorsList = document.querySelectorAll(".hidden-author");

const showAuthor = () => {
  for (const author of authorsList) {
    if (author.offsetTop < (window.scrollY + window.innerHeight / 1.2)) {
      author.classList.remove("hidden-author");
    }
  }
}

showAuthor();
document.addEventListener("scroll", showAuthor);