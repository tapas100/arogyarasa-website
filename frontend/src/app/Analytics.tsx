import Script from "next/script";

export default function Analytics(){
  return (
    <>
      {/* Example: Plausible analytics – replace with your own domain */}
      <Script
        async
        src="https://plausible.io/js/plausible.js"
        data-domain="arogyarasa.com"
      />
    </>
  );
}
