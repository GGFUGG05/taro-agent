import Head from 'next/head';
import TarotReading from '../components/TarotReading';
import styles from '../styles/Home.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Taro Tarot Reader</title>
        <meta name="description" content="Taro Tarot Reader powered by AI" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <TarotReading />
      </main>

      <footer className={styles.footer}>
        <p>
          Powered by Next.js, FastAPI, and OpenAI
        </p>
      </footer>
    </div>
  );
}