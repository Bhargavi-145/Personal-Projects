document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById("menu-btn");
    const navbar = document.querySelector(".navbar");

    // Toggle navigation menu on mobile
    menuBtn.addEventListener("click", function () {
        navbar.classList.toggle("show");
    });

    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll(".navbar a");
    navLinks.forEach((link) => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            window.scrollTo({
                top: targetElement.offsetTop - navbar.clientHeight,
                behavior: "smooth"
            });

            // Close the navigation menu on mobile
            navbar.classList.remove("show");
        });
    });
});
