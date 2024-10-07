/* script.js */
document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    document.body.classList.add(currentTheme);
    document.getElementById('theme-toggle').innerText = currentTheme === 'dark-mode' ? 'Switch to Light Mode' : 'Switch to Dark Mode';

    toggleBtn.addEventListener('click', () => {
        if (document.body.classList.contains('dark-mode')) {
            document.body.classList.replace('dark-mode', 'light-mode');
            toggleBtn.innerText = 'Switch to Dark Mode';
            localStorage.setItem('theme', 'light-mode');
        } else {
            document.body.classList.replace('light-mode', 'dark-mode');
            toggleBtn.innerText = 'Switch to Light Mode';
            localStorage.setItem('theme', 'dark-mode');
        }
    });
});
