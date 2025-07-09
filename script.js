document.addEventListener('DOMContentLoaded', () => {
    console.log('SRKREC_IKYA website loaded!');

    // Smooth scroll to a section when a button is clicked
    const buttons = document.querySelectorAll('button, a[data-target]');
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent any default button behavior

            const targetId = button.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.style.display = 'block';
                targetElement.scrollIntoView({ behavior: 'smooth' });
            } else {
                console.warn(`Target section with ID "${targetId}" not found.`);
            }
        });
    });
});
