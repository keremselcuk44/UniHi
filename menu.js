async function fetchMenuData() {
    try {
        const response = await fetch('menu_data.json');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Menü verisi alınırken hata oluştu:', error);
        return null;
    }
}

function updateLikes(menuId, action, type) {
    const likeCount = document.getElementById(`${type}-like-count-${menuId}`);
    const dislikeCount = document.getElementById(`${type}-dislike-count-${menuId}`);
    const likeBtn = document.getElementById(`${type}-like-btn-${menuId}`);
    const dislikeBtn = document.getElementById(`${type}-dislike-btn-${menuId}`);
    
    if (action === 'like') {
        if (likeBtn.classList.contains('bg-green-500')) {
            likeBtn.classList.remove('bg-green-500');
            likeCount.textContent = parseInt(likeCount.textContent) - 1;
        } else {
            likeBtn.classList.add('bg-green-500');
            likeCount.textContent = parseInt(likeCount.textContent) + 1;
            if (dislikeBtn.classList.contains('bg-red-500')) {
                dislikeBtn.classList.remove('bg-red-500');
                dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
            }
        }
    } else {
        if (dislikeBtn.classList.contains('bg-red-500')) {
            dislikeBtn.classList.remove('bg-red-500');
            dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
        } else {
            dislikeBtn.classList.add('bg-red-500');
            dislikeCount.textContent = parseInt(dislikeCount.textContent) + 1;
            if (likeBtn.classList.contains('bg-green-500')) {
                likeBtn.classList.remove('bg-green-500');
                likeCount.textContent = parseInt(likeCount.textContent) - 1;
            }
        }
    }
}

function createMenuElement(item, index, type) {
    const li = document.createElement('li');
    li.className = 'bg-gray-100 p-4 rounded-lg shadow-md flex-1 min-w-[200px] max-w-[300px]';
    
    const menuContent = document.createElement('div');
    menuContent.className = 'text-center font-medium text-gray-800 mb-2';
    menuContent.textContent = typeof item === 'string' ? item : `${item.category}: ${item.name}`;
    li.appendChild(menuContent);
    
    const buttonsContainer = document.createElement('div');
    buttonsContainer.className = 'flex justify-center space-x-4 mt-2';
    
    const likeBtn = document.createElement('button');
    likeBtn.className = 'flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-green-500 hover:text-white transition-colors';
    likeBtn.onclick = () => updateLikes(index, 'like', type);
    likeBtn.id = `${type}-like-btn-${index}`;
    
    const likeIcon = document.createElement('span');
    likeIcon.className = 'text-lg';
    likeIcon.textContent = '👍';
    
    const likeCount = document.createElement('span');
    likeCount.id = `${type}-like-count-${index}`;
    likeCount.textContent = '0';
    
    likeBtn.appendChild(likeIcon);
    likeBtn.appendChild(likeCount);
    
    const dislikeBtn = document.createElement('button');
    dislikeBtn.className = 'flex items-center space-x-1 px-3 py-1 rounded-full bg-gray-200 hover:bg-red-500 hover:text-white transition-colors';
    dislikeBtn.onclick = () => updateLikes(index, 'dislike', type);
    dislikeBtn.id = `${type}-dislike-btn-${index}`;
    
    const dislikeIcon = document.createElement('span');
    dislikeIcon.className = 'text-lg';
    dislikeIcon.textContent = '👎';
    
    const dislikeCount = document.createElement('span');
    dislikeCount.id = `${type}-dislike-count-${index}`;
    dislikeCount.textContent = '0';
    
    dislikeBtn.appendChild(dislikeIcon);
    dislikeBtn.appendChild(dislikeCount);
    
    buttonsContainer.appendChild(likeBtn);
    buttonsContainer.appendChild(dislikeBtn);
    li.appendChild(buttonsContainer);
    
    return li;
}

async function updateMenuDisplay() {
    const menuData = await fetchMenuData();
    if (!menuData) return;
    
    // Üniversite menüsünü güncelle
    const uniMenuSection = document.getElementById('gunun-menusu');
    if (uniMenuSection) {
        const dateElement = uniMenuSection.querySelector('p');
        if (dateElement) dateElement.textContent = menuData.uni_menu.date;
        
        const menuList = uniMenuSection.querySelector('ul');
        if (menuList) {
            menuList.innerHTML = '';
            menuData.uni_menu.items.forEach((item, index) => {
                menuList.appendChild(createMenuElement(item, index, 'uni'));
            });
        }
    }
    
    // KYK akşam menüsünü güncelle
    const kykMenuSection = document.getElementById('kyk-menu');
    if (kykMenuSection && menuData.kyk_menus.aksam) {
        const menuList = kykMenuSection.querySelector('ul');
        if (menuList) {
            menuList.innerHTML = '';
            Object.entries(menuData.kyk_menus.aksam).forEach(([category, item], index) => {
                menuList.appendChild(createMenuElement({ category, name: item }, index, 'kyk'));
            });
        }
    }
    
    // KYK kahvaltı menüsünü güncelle
    const kykSabahMenuSection = document.getElementById('kyk-sabah-menu');
    if (kykSabahMenuSection && menuData.kyk_menus.sabah) {
        const menuList = kykSabahMenuSection.querySelector('ul');
        if (menuList) {
            menuList.innerHTML = '';
            menuData.kyk_menus.sabah.menü.forEach((item, index) => {
                let menuText = item.isim;
                if (item.gramaj) menuText += ` (${item.gramaj})`;
                else if (item.adet) menuText += ` (${item.adet} adet)`;
                if (item.ek) menuText += ` - ${item.ek}`;
                menuList.appendChild(createMenuElement(menuText, index, 'kyk-sabah'));
            });
        }
    }
    
    // Son güncelleme zamanını göster
    const lastUpdated = document.getElementById('last-updated');
    if (lastUpdated) {
        lastUpdated.textContent = `Son güncelleme: ${menuData.last_updated}`;
    }
}

// Sayfa yüklendiğinde menüyü güncelle
document.addEventListener('DOMContentLoaded', updateMenuDisplay);

// Her 5 dakikada bir menüyü güncelle
setInterval(updateMenuDisplay, 5 * 60 * 1000); 