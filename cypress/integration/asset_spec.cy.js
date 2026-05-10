describe('Asset loading', () => {
  it('should load all local images on the homepage', () => {
    cy.visit('https://tapas100.github.io/arogyarasa-website/')
    const assets = [
      'assets/farm.jpg',
      'assets/farm.svg',
      'assets/sundry.jpg',
      'assets/grind.jpg',
      'assets/heart.jpg',
      'assets/sun.svg',
      'assets/mortar.svg',
      'assets/handheart.svg'
    ];
    assets.forEach(src => {
      cy.get(`img[src="${src}"]`).should('be.visible');
    });
  });
});