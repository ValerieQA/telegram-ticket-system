'use client';

import { useEffect } from 'react';

import { ArtistSection } from '@/components/ArtistSection';
import { CarouselSection } from '@/components/CarouselSection';
import { HeroSection } from '@/components/HeroSection';
import { MediaSection } from '@/components/MediaSection';
import { initTelegramWebApp } from '@/lib/telegram';

export default function Home() {
  useEffect(() => {
    initTelegramWebApp();
  }, []);

  return (
    <main className="container">
      <HeroSection />
      <ArtistSection />
      <CarouselSection />
      <MediaSection />
    </main>
  );
}
