import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Introduction
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Physical AI & Humanoid Robotics Course">
      
      <HomepageHeader />

      <main className="container" style={{ padding: '2rem 0' }}>
        <h2>Modules</h2>
        <ul style={{ listStyle: 'none', paddingLeft: 0, display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <li>
            <Link className="button button--secondary" to="/docs/module1">
              Module 1
            </Link>
          </li>
          <li>
            <Link className="button button--secondary" to="/docs/module2">
              Module 2
            </Link>
          </li>
          <li>
            <Link className="button button--secondary" to="/docs/module3">
              Module 3
            </Link>
          </li>
          <li>
            <Link className="button button--secondary" to="/docs/module4">
              Module 4
            </Link>
          </li>
        </ul>

        <h2 style={{ marginTop: '2rem' }}>Assessment</h2>
        <ul style={{ listStyle: 'none', paddingLeft: 0 }}>
          <li>
            <Link className="button button--primary" to="/docs/assessment">
              Final Assessment
            </Link>
          </li>
        </ul>
      </main>
    </Layout>
  );
}
