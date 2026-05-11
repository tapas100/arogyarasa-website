import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Hero from "@/components/Hero";
import ProductCard from "@/components/ProductCard";

export default function Home(){
  const products=[
    {img:"/assets/turmeric.jpg",title:"Turmeric Gold",desc:"Anti‑inflammatory, vibrant colour – perfect for curries and wellness drinks."},
    {img:"/assets/cinnamon.jpg",title:"Cinnamon Whisper",desc:"Sweet, aromatic, heart‑healthy – ideal for desserts and teas."},
    {img:"/assets/pepper.jpg",title:"Black Pepper Zest",desc:"Robust pungency that elevates every savory dish."},
    {img:"/assets/chili.jpg",title:"Chili Fire",desc:"Fiery heat with a smoky finish – for the bold palate."},
  ];
  return (
    <>
      <Header/>
      <Hero/>
      <section id="products" className="bg-bg py-16">
        <div className="container mx-auto px-4">
          <h2 className="font-heading text-3xl text-center mb-8">Featured Spices</h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {products.map((p,i)=><ProductCard key={i} img={p.img} title={p.title} desc={p.desc}/>)}
          </div>
        </div>
      </section>
      <Footer/>
    </>
  );
}
