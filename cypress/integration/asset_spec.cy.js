describe('Asset loading', () => {
  it('should load all local images on the homepage', () => {
    cy.visit('https://tapas100.github.io/arogyarasa-website/')
    const assets = [
      'assets/farm.jpg',
      'assets/farm.svg',
      'assets/turmeric.jpg',
      'assets/cinnamon.jpg',
      'assets/pepper.jpg',
      'assets/chili.jpg',
      'assets/grind.jpg',
      'assets/sun.svg',
      'assets/mortar.svg',
      'assets/handheart.svg',
      'assets/sundry.jpg'
    ];
    assets.forEach(src => {
      cy.get(`img[src="${src}"]`).should('be.visible');
    });
  });
});