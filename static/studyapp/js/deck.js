document.querySelectorAll('.carousel-control-prev').forEach(button => {
    button.addEventListener('click', () => {
        const activeItem = document.querySelector('.carousel-item.active');
        const prevItem = activeItem.previousElementSibling || document.querySelector('.carousel-item:last-child');
        
        activeItem.classList.remove('active');
        prevItem.classList.add('active');
    });
});

document.querySelectorAll('.carousel-control-next').forEach(button => {
    button.addEventListener('click', () => {
        const activeItem = document.querySelector('.carousel-item.active');
        const nextItem = activeItem.nextElementSibling || document.querySelector('.carousel-item:first-child');
        
        activeItem.classList.remove('active');
        nextItem.classList.add('active');
    });
});