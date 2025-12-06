// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    'intro', // intro page first
    {
      type: 'category',
      label: 'Modules',
      items: ['module1', 'module2', 'module3', 'module4'],
    },
    {
      type: 'category',
      label: 'Assessment',
      items: ['assessment'],
    },
  ],
};

export default sidebars;
