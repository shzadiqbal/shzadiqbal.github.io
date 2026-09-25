document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');

    if (menuToggle && nav) {
        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('show');
        });
    }

    // 2. Publication Filter Tabs (publications.html)
    const tabButtons = document.querySelectorAll('.tab-btn');
    const pubGroups = document.querySelectorAll('.pub-group');

    if (tabButtons.length > 0) {
        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                tabButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                const filter = button.getAttribute('data-filter');

                pubGroups.forEach(group => {
                    if (filter === 'all') {
                        group.style.display = 'block';
                    } else {
                        const category = group.getAttribute('data-category');
                        if (category === filter) {
                            group.style.display = 'block';
                        } else {
                            group.style.display = 'none';
                        }
                    }
                });
            });
        });
    }

    // 3. Header Elevation on Scroll
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.06)';
        } else {
            header.style.boxShadow = 'none';
        }
    });
});