// Profile data management
let userData = {
    name: '',
    faculty: '',
    department: '',
    photoUrl: 'photos/profil.png'
};

// Load saved user data on page load
document.addEventListener('DOMContentLoaded', () => {
    loadUserData();
    setupEventListeners();
    updateUIWithUserData();
});

// Load user data from localStorage
function loadUserData() {
    const savedData = localStorage.getItem('userData');
    if (savedData) {
        const parsedData = JSON.parse(savedData);
        userData = {
            name: parsedData.name || '',
            faculty: parsedData.faculty || '',
            department: parsedData.department || '',
            photoUrl: parsedData.photoUrl || 'photos/profil.png'
        };
    }
}

// Save user data to localStorage
function saveUserData() {
    localStorage.setItem('userData', JSON.stringify(userData));
}

// Update UI elements with user data
function updateUIWithUserData() {
    // Update profile pictures across all pages
    const profileImages = document.querySelectorAll('.profile-menu img');
    profileImages.forEach(img => {
        img.src = userData.photoUrl;
    });

    // Update settings page fields if we're on that page
    if (window.location.pathname.includes('settings.html')) {
        const profilePreview = document.getElementById('profilePreview');
        const nameInput = document.getElementById('nameInput');
        const facultyInput = document.getElementById('facultyInput');
        const departmentInput = document.getElementById('departmentInput');

        if (profilePreview) {
            profilePreview.src = userData.photoUrl;
        }
        if (nameInput) nameInput.value = userData.name || '';
        if (facultyInput) facultyInput.value = userData.faculty || '';
        if (departmentInput) departmentInput.value = userData.department || '';
    }
}

// Set up event listeners for the settings page
function setupEventListeners() {
    if (!window.location.pathname.includes('settings.html')) return;

    const photoInput = document.getElementById('photoInput');
    const saveButton = document.getElementById('saveButton');
    const nameInput = document.getElementById('nameInput');
    const facultyInput = document.getElementById('facultyInput');
    const departmentInput = document.getElementById('departmentInput');
    const passwordInput = document.getElementById('passwordInput');
    const confirmPasswordInput = document.getElementById('confirmPasswordInput');

    // Handle photo upload
    photoInput?.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const newPhotoUrl = e.target.result;
                userData.photoUrl = newPhotoUrl;
                
                // Update preview immediately
                const profilePreview = document.getElementById('profilePreview');
                if (profilePreview) {
                    profilePreview.src = newPhotoUrl;
                }
                
                // Save to localStorage immediately
                saveUserData();
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle save button click
    saveButton?.addEventListener('click', () => {
        // Validate password change if attempted
        if (passwordInput.value || confirmPasswordInput.value) {
            if (passwordInput.value !== confirmPasswordInput.value) {
                alert('Şifreler eşleşmiyor!');
                return;
            }
            // Here you would typically handle password change
            // For demo purposes, we'll just clear the fields
            passwordInput.value = '';
            confirmPasswordInput.value = '';
        }

        // Update user data
        userData.name = nameInput.value;
        userData.faculty = facultyInput.value;
        userData.department = departmentInput.value;

        // Save to localStorage
        saveUserData();
        
        // Update UI
        updateUIWithUserData();

        alert('Değişiklikler kaydedildi!');
    });
}

// Update profile data when page loads
updateUIWithUserData(); 