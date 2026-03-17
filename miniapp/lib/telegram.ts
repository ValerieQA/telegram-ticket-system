export function initTelegramWebApp(): void {
  if (typeof window === 'undefined') return;

  const tg = (window as any).Telegram?.WebApp;
  if (!tg) return;

  tg.ready();
  tg.expand();
  tg.MainButton.hide();
}
