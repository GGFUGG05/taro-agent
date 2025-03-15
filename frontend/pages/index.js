import Head from 'next/head';
import TaroChat from '../components/TaroChat';
import styles from '../styles/Home.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Taro AI Agent</title>
        <meta name="description" content="Unveal your destiny" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Taro AI Agent</h1>
        <p className={styles.description}>
          Unveal your destiny
        </p>
        
        <TaroChat />
      </main>

      <footer className={styles.footer}>
        <p>
          Powered by Next.js, FastAPI, and OpenAI
        </p>
      </footer>
    </div>
  );
}