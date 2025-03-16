import Head from 'next/head';
import TarotReading from '../components/TarotReading';
import styles from '../styles/Home.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>The Tarot Oracle</title>
        <meta name="description" content="Tarot Reader powered by AI" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <TarotReading />
      </main>

    </div>
  );
}