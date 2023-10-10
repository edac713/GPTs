// Map collection names to carousel IDs
const collectionToCarouselMap = {
  "patches": "patches-all-carousel",
  "patches-nascar-drivers-teams": "patches-nascar-drivers-teams-carousel",
  "patches-speedways-racing-series": "patches-speedways-racing-series-carousel",
  "patches-ag-farming": "patches-ag-farming-carousel",
  "patches-beer-liquor": "patches-beer-liquor-carousel",
  "patches-car-truck-brands": "patches-car-truck-brands-carousel",
  "patches-racing-brands": "patches-racing-brands-carousel",
  "patches-diesel": "patches-diesel-carousel",
  "patches-drag-racing": "patches-drag-racing-carousel",
  "patches-hunting-fishing-guns": "patches-hunting-fishing-guns-carousel",
  "patches-motorcycle-brands": "patches-motorcycle-brands-carousel",
  "patches-national-parks": "patches-national-parks-carousel",
  "patches-miscellaneous": "patches-miscellaneous-carousel",
  //...other patch collections
  "hats": "hats-all-carousel",
  "richardson": "hats-richardson-carousel",
  "imperial": "hats-imperial-carousel",
  "yupoong": "hats-yupoong-carousel",
  "pacific": "hats-pacific-carousel"
  //...other hat collections
};

// Show target carousel, hide others 
function showCarousel(carouselId) {

  // Hide all patch carousels
  $(".patch-carousel").hide();

  // Hide all hat carousels
  $(".hat-carousel").hide();

  $("#" + carouselId).show();

}

// Handle collection clicks
function handleCollectionClick() {

  // Get collection name
  const collection = $(this).data("collection");

  // Get carousel ID
  const carouselId = collectionToCarouselMap[collection];

  // Show carousel
  showCarousel(carouselId);

}

$(document).ready(function () {

  // Collection click handler
  $(".collection").on("click", handleCollectionClick);

  // Initialize patch carousels
  $(".patch-carousel").slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    centerMode: true,
    arrows: false,
    adaptiveHeight: false,
    variableWidth: true
  });

  // Initialize hat carousels
  $(".hat-carousel").slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    centerMode: true,
    arrows: false,
    adaptiveHeight: false,
    variableWidth: true
  }).slick('slickPause');

  // SVG content for play and pause
  const playSVG = `<svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M13.875 10.65a.75.75 0 0 0 0-1.3l-5.25-3.03a.75.75 0 0 0-1.125.649v6.062a.75.75 0 0 0 1.125.65l5.25-3.032Zm-4.875 1.082v-3.464l3 1.732-3 1.732Z" fill="#332E21"/><path fill-rule="evenodd" d="M10 3a7 7 0 1 0 0 14 7 7 0 0 0 0-14Zm-5.5 7a5.5 5.5 0 1 1 11 0 5.5 5.5 0 0 1-11 0Z" fill="#332E21"/></svg>`;
  const pauseSVG = `<svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M8 7.25a.75.75 0 0 1 .75.75v4a.75.75 0 0 1-1.5 0v-4a.75.75 0 0 1 .75-.75Z" fill="#332E21"/><path d="M12.75 8a.75.75 0 0 0-1.5 0v4a.75.75 0 0 0 1.5 0v-4Z" fill="#332E21"/><path fill-rule="evenodd" d="M10 17a7 7 0 1 0 0-14 7 7 0 0 0 0 14Zm0-1.5a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11Z" fill="#332E21"/></svg>`;

  // Handle play/pause functionality for carousels
  $('#playPauseIcon').on('click', function () {
    if ($(this).attr('data-state') === 'playing') {
      $('.default-patch-carousel, .default-hat-carousel').slick('slickPause');
      $(this).attr('data-state', 'paused');
      $(this).html(playSVG);
    } else {
      if ($('#patchesToggle').hasClass('active')) {
        $('.default-patch-carousel').slick('slickPlay');
      } else {
        $('.default-hat-carousel').slick('slickPlay');
      }
      $(this).attr('data-state', 'playing');
      $(this).html(pauseSVG);
    }
  });

  // Handle toggle click event for switching carousels
  $('#patchesToggle, #hatsToggle').on('click', function () {
    if ($(this).hasClass('active')) return;

    $('.toggle-button').removeClass('active');
    $(this).addClass('active');

    toggleCarouselPlayback();
    updateHatBuilderHeader();

    if ($('#hatsToggle').hasClass('active')) {
      $('.active-background').css('left', '49%');
    } else {
      $('.active-background').css('left', '1%');
    }

    if ($('#patchesToggle').hasClass('active')) {
      $('#patchHighlight').show();
      $('#hatHighlight').hide();
    } else {
      $('#hatHighlight').show();
      $('#patchHighlight').hide();
    }
  });

  // Update header label based on active carousel
  function updateHatBuilderHeader() {
    const isPatchesActive = $('#patchesToggle').hasClass('active');
    const label = isPatchesActive ? "All Patches" : "All Hats";
    $('.hat-builder-collection-label').text(label);
  }

  // Set initial category display based on active carousel
  function setInitialCategoryDisplay() {
    if ($('#patchesToggle').hasClass('active')) {
      $('#shopify-section-template--14833441800262__81fbde0d-26af-45a0-bc7b-b0514d8bd082 .collection-list').show();
      $('#shopify-section-template--14833441800262__e617045b-0ee9-4ffa-a5a4-a21a2ccd0cf6 .collection-list').hide();
    } else {
      $('#shopify-section-template--14833441800262__81fbde0d-26af-45a0-bc7b-b0514d8bd082 .collection-list').hide();
      $('#shopify-section-template--14833441800262__e617045b-0ee9-4ffa-a5a4-a21a2ccd0cf6 .collection-list').show();
    }
  }

  setInitialCategoryDisplay();

  // Scroll to hat builder container on button click
  $('#scrollButton').on('click', function () {
    const targetScroll = $(".hat-builder-container").offset().top;
    $('html, body').animate({
      scrollTop: targetScroll
    }, 1000);
  });

});
