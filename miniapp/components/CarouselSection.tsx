'use client';

import { useState } from 'react';

const slides = ['VIP Experience', 'Backstage Stories', 'Crowd Moments'];

export function CarouselSection() {
  const [index, setIndex] = useState(0);

  const next = () => setIndex((i) => (i + 1) % slides.length);
  const prev = () => setIndex((i) => (i - 1 + slides.length) % slides.length);

  return (
    <section className="card">
      <div className="carousel-header">
        <h2>Highlights</h2>
        <div className="arrows">
          <button onClick={prev} aria-label="Previous slide">←</button>
          <button onClick={next} aria-label="Next slide">→</button>
        </div>
      </div>
      <div className="slide">{slides[index]}</div>
    </section>
  );
}
