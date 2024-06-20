(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });

    
    $(document).ready(function () {
      // Função para carregar as propriedades
      function fetchProperties(status) {
          $.ajax({
              url: "{% url 'property_list' %}",
              data: {
                  status: status
              },
              success: function (data) {
                  var propertyList = $('.property_list');
                  propertyList.empty();

                  data.properties.forEach(function(property) {
                      var propertyItem = `
                          <div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                              <div class="property-item rounded overflow-hidden">
                                  <div class="position-relative overflow-hidden">
                                      <a href=""><img class="img-fluid" src="${property.image}" alt=""></a>
                                      <div class="bg-primary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3">${property.status}</div>
                                      <div class="bg-white rounded-top text-primary position-absolute start-0 bottom-0 mx-4 pt-1 px-3">${property.housing}</div>
                                  </div>
                                  <div class="p-4 pb-0">
                                      <h5 class="text-primary mb-3">${property.price}</h5>
                                      <a class="d-block h5 mb-2" href="">${property.property_listing}</a>
                                      <p><i class="fa fa-map-marker-alt text-primary me-2"></i>${property.street_number} Street, ${property.city}, ${property.country}</p>
                                  </div>
                                  <div class="d-flex border-top">
                                      <small class="flex-fill text-center border-end py-2"><i class="fa fa-ruler-combined text-primary me-2"></i>${property.area} Sqft</small>
                                      <small class="flex-fill text-center border-end py-2"><i class="fa fa-bed text-primary me-2"></i>${property.bedrooms} Bed</small>
                                      <small class="flex-fill text-center py-2"><i class="fa fa-bath text-primary me-2"></i>${property.bathrooms} Bath</small>
                                  </div>
                              </div>
                          </div>
                      `;
                      propertyList.append(propertyItem);
                  });
              },
              error: function (error) {
                  console.error("Error fetching properties:", error);
              }
          });
      }

      // Chama a função para carregar as propriedades inicialmente (todos)
      fetchProperties('all'); 

      // Filtra as propriedades quando os botões são clicados
      $('[data-bs-toggle="pill"]').click(function (e) {
          e.preventDefault();
          var status = $(this).data('status'); // Obtém o status do botão

          fetchProperties(status);
      });
  });


    document.addEventListener('DOMContentLoaded', function() {
        const pagination = document.getElementById('pagination');
        const prevButton = pagination.querySelector('.prev');
        const nextButton = pagination.querySelector('.next');
        const pagesContainer = pagination.querySelector('.pages');
        let currentPage = 1;

        prevButton.addEventListener('click', function(e) {
            e.preventDefault();
            if (currentPage > 1) {
                currentPage--;
                updatePagination();
            }
        });

        nextButton.addEventListener('click', function(e) {
            e.preventDefault();
            currentPage++;
            updatePagination();
        });

        function updatePagination() {
            const totalItems = 10; // Suponha que haja 10 páginas no total
            const totalPages = Math.ceil(totalItems / 4); // Calcula o número total de páginas

            pagesContainer.innerHTML = ''; // Limpa o conteúdo anterior das páginas

            let startPage = Math.max(1, currentPage - 1); // Calcula a página inicial a ser mostrada
            let endPage = Math.min(totalPages, startPage + 3); // Calcula a página final a ser mostrada

            for (let i = startPage; i <= endPage; i++) {
                const pageLink = document.createElement('a');
                pageLink.href = '#';
                pageLink.classList.add('page-link');
                pageLink.textContent = i;
                if (i === currentPage) {
                    pageLink.classList.add('active');
                }
                pagesContainer.appendChild(pageLink);
            }
        }

        // Inicializa a paginação
        updatePagination();
    });


})(jQuery);


