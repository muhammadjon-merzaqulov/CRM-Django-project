// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');

    if (userMenuButton && userMenu) {
        userMenuButton.addEventListener('click', function() {
            userMenu.classList.toggle('hidden');
        });

        // Close the menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
                userMenu.classList.add('hidden');
            }
        });
    }

    // Mobile sidebar toggle
    const mobileSidebarButton = document.getElementById('mobile-sidebar-button');
    const sidebar = document.querySelector('aside');

    if (mobileSidebarButton && sidebar) {
        mobileSidebarButton.addEventListener('click', function() {
            sidebar.classList.toggle('hidden');
            sidebar.classList.toggle('fixed');
            sidebar.classList.toggle('inset-0');
            sidebar.classList.toggle('z-40');
        });
    }

    // Flash messages auto-dismiss
    const flashMessages = document.querySelectorAll('.messages .alert');

    if (flashMessages.length > 0) {
        flashMessages.forEach(message => {
            // Auto-dismiss after 5 seconds
            setTimeout(() => {
                message.style.opacity = '0';
                setTimeout(() => {
                    message.style.display = 'none';
                }, 300);
            }, 5000);

            // Close button
            const closeButton = message.querySelector('button');
            if (closeButton) {
                closeButton.addEventListener('click', () => {
                    message.style.opacity = '0';
                    setTimeout(() => {
                        message.style.display = 'none';
                    }, 300);
                });
            }
        });
    }

    // Tab functionality
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    if (tabBtns.length > 0 && tabContents.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all buttons
                tabBtns.forEach(b => {
                    b.classList.remove('active', 'border-blue-500', 'text-blue-600');
                    b.classList.add('text-gray-500');
                });

                // Add active class to clicked button
                btn.classList.add('active', 'border-blue-500', 'text-blue-600');
                btn.classList.remove('text-gray-500');

                // Hide all tab contents
                tabContents.forEach(content => {
                    content.classList.add('hidden');
                });

                // Show the selected tab content
                const tabId = btn.getAttribute('data-tab');
                document.getElementById(`${tabId}-tab`).classList.remove('hidden');
            });
        });
    }

    // Date range picker initialization
    const dateRangePickers = document.querySelectorAll('.date-range-picker');

    if (dateRangePickers.length > 0) {
        dateRangePickers.forEach(picker => {
            // Initialize date range picker if needed
            // This is a placeholder for a date range picker library
            console.log('Date range picker initialized');
        });
    }

    // Form validation
    const forms = document.querySelectorAll('form');

    if (forms.length > 0) {
        forms.forEach(form => {
            form.addEventListener('submit', function(event) {
                const requiredFields = form.querySelectorAll('[required]');
                let isValid = true;

                requiredFields.forEach(field => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.classList.add('border-red-500');

                        // Add error message if not exists
                        const errorMessage = field.parentNode.querySelector('.error-message');
                        if (!errorMessage) {
                            const message = document.createElement('p');
                            message.classList.add('text-red-500', 'text-xs', 'mt-1', 'error-message');
                            message.textContent = 'This field is required';
                            field.parentNode.appendChild(message);
                        }
                    } else {
                        field.classList.remove('border-red-500');

                        // Remove error message if exists
                        const errorMessage = field.parentNode.querySelector('.error-message');
                        if (errorMessage) {
                            errorMessage.remove();
                        }
                    }
                });

                if (!isValid) {
                    event.preventDefault();
                }
            });
        });
    }

    // Search functionality enhancement
    const searchInputs = document.querySelectorAll('input[type="search"], input#search');

    if (searchInputs.length > 0) {
        searchInputs.forEach(input => {
            // Add clear button
            const wrapper = document.createElement('div');
            wrapper.classList.add('relative');

            const clearButton = document.createElement('button');
            clearButton.type = 'button';
            clearButton.classList.add('absolute', 'right-10', 'top-1/2', 'transform', '-translate-y-1/2', 'text-gray-400', 'hover:text-gray-600', 'hidden');
            clearButton.innerHTML = '<i class="fas fa-times"></i>';

            input.parentNode.insertBefore(wrapper, input);
            wrapper.appendChild(input);
            wrapper.appendChild(clearButton);

            // Show/hide clear button
            input.addEventListener('input', function() {
                if (this.value) {
                    clearButton.classList.remove('hidden');
                } else {
                    clearButton.classList.add('hidden');
                }
            });

            // Clear input
            clearButton.addEventListener('click', function() {
                input.value = '';
                input.focus();
                clearButton.classList.add('hidden');

                // Trigger input event to update any filters
                const inputEvent = new Event('input', { bubbles: true });
                input.dispatchEvent(inputEvent);
            });
        });
    }
});