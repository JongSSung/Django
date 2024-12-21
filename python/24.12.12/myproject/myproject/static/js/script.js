document.addEventListener('DOMContentLoaded', function() {
    var dropdownToggles = document.querySelectorAll('.dropdown-toggle_dep1');
    
    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(event) {
            event.preventDefault();
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            } else {
                dropdownContent.style.display = 'block';
            }
        });
    });

    // 클릭 외부 영역 클릭 시 드롭다운 메뉴 닫기
    document.addEventListener('click', function(event) {
        dropdownToggles.forEach(function(toggle) {
            var dropdownContent = toggle.nextElementSibling;
            if (dropdownContent.style.display === 'block' && !toggle.contains(event.target) && !dropdownContent.contains(event.target)) {
                dropdownContent.style.display = 'none';
            }
        });
    });
});