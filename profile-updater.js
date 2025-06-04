// Profile data management
let userData = {
    name: '',
    faculty: '',
    department: '',
    photoUrl: 'photos/profil.png'
};

// Sayfa yüklendiğinde çalışacak fonksiyon
document.addEventListener('DOMContentLoaded', function() {
    // localStorage'dan veriyi yükle
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

    // Profil resimlerini güncelle
    updateProfileImages();
    
    // Settings sayfası için event listener'ları ayarla
    if (window.location.pathname.includes('settings.html')) {
        setupSettingsPage();
    }
});

// Profil resimlerini güncelle
function updateProfileImages() {
    const profileImages = document.querySelectorAll('.profile-menu img');
    profileImages.forEach(img => {
        // Resim yüklenme hatası durumunda varsayılan resmi göster
        img.onerror = function() {
            this.src = 'photos/profil.png';
        };
        // Resmi ayarla
        img.src = userData.photoUrl;
    });

    // Settings sayfasındaki önizleme resmini güncelle
    const profilePreview = document.getElementById('profilePreview');
    if (profilePreview) {
        profilePreview.onerror = function() {
            this.src = 'photos/profil.png';
        };
        profilePreview.src = userData.photoUrl;
    }
}

// Settings sayfası için event listener'ları ayarla
function setupSettingsPage() {
    const photoInput = document.getElementById('photoInput');
    const saveButton = document.getElementById('saveButton');
    const nameInput = document.getElementById('nameInput');
    const facultyInput = document.getElementById('facultyInput');
    const departmentInput = document.getElementById('departmentInput');
    const passwordInput = document.getElementById('passwordInput');
    const confirmPasswordInput = document.getElementById('confirmPasswordInput');

    // Form alanlarını doldur
    if (nameInput) nameInput.value = userData.name;
    if (facultyInput) facultyInput.value = userData.faculty;
    if (departmentInput) departmentInput.value = userData.department;

    // Fotoğraf yükleme
    photoInput?.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                userData.photoUrl = e.target.result;
                localStorage.setItem('userData', JSON.stringify(userData));
                updateProfileImages();
            };
            reader.readAsDataURL(file);
        }
    });

    // Kaydet butonu
    saveButton?.addEventListener('click', () => {
        if (passwordInput.value || confirmPasswordInput.value) {
            if (passwordInput.value !== confirmPasswordInput.value) {
                alert('Şifreler eşleşmiyor!');
                return;
            }
            passwordInput.value = '';
            confirmPasswordInput.value = '';
        }

        userData.name = nameInput.value;
        userData.faculty = facultyInput.value;
        userData.department = departmentInput.value;

        localStorage.setItem('userData', JSON.stringify(userData));
        updateProfileImages();
        alert('Değişiklikler kaydedildi!');
    });
} 