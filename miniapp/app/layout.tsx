import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Telegram Ticket Mini App',
  description: 'Landing page + purchase interface for Telegram ticketing.'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
