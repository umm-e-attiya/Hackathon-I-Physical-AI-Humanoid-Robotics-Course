// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics Course',
  tagline: 'A complete course on embodied intelligence, humanoid robotics, and AI systems in the physical world.',
  favicon: 'img/favicon.ico',
  future: {
    v4: true,
  },
  url: 'https://anthropic.github.io',
  baseUrl: '/',
  organizationName: 'anthropic',
  projectName: 'book',
  onBrokenLinks: 'throw',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Course Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          label: 'Introduction',   // Changed from 'Intro'
          to: '/docs/intro',
          position: 'left',
        },
        {
          label: 'Modules',
          position: 'left',
          items: [
            { label: 'Module 1', to: '/docs/module1' },
            { label: 'Module 2', to: '/docs/module2' },
            { label: 'Module 3', to: '/docs/module3' },
            { label: 'Module 4', to: '/docs/module4' },
          ],
        },
        {
          label: 'Assessment',
          to: '/docs/assessment',
          position: 'left',
        },
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Introduction', to: '/docs/intro' }, // Changed from 'Intro'
            { label: 'Module 1', to: '/docs/module1' },
            { label: 'Module 2', to: '/docs/module2' },
            { label: 'Module 3', to: '/docs/module3' },
            { label: 'Module 4', to: '/docs/module4' },
            { label: 'Assessment', to: '/docs/assessment' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Stack Overflow', href: 'https://stackoverflow.com/questions/tagged/docusaurus' },
            { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
            { label: 'X', href: 'https://x.com/docusaurus' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: '/blog' },
            { label: 'GitHub', href: 'https://github.com/facebook/docusaurus' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Course. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
