import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import {
  CheckCircle2,
  MapPin,
  PhoneCall,
  Mail,
  Menu,
  X,
  ArrowRight,
  ShieldCheck,
  Droplets,
  ClipboardCheck,
  Home as HomeIcon,
  ChevronRight,
  Clock,
  Star,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

import logoSrc from "@/assets/logo_svg.svg";
import brandBanner from "@/assets/brand_banner.png";
import beforeAfterDrive from "@/assets/before_after_drive.png";
import beforeAfterPatio from "@/assets/before_after_patio.png";
import beforeAfterRender from "@/assets/before_after_render.png";
import beforeAfterGutter from "@/assets/before_after_gutter.png";

const formSchema = z.object({
  name: z.string().min(2, "Name is required"),
  phone: z.string().min(10, "Valid phone number required"),
  email: z.string().email("Valid email required"),
  postcode: z.string().min(5, "Postcode is required"),
  service: z.string().min(1, "Please select a service"),
  message: z.string().optional(),
});

const fadeUp = {
  hidden: { opacity: 0, y: 28 },
  visible: (i = 0) => ({
    opacity: 1,
    y: 0,
    transition: { duration: 0.55, delay: i * 0.1, ease: "easeOut" },
  }),
};

export default function Home() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    document.documentElement.classList.add("dark");
    const handleScroll = () => setIsScrolled(window.scrollY > 50);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: { name: "", phone: "", email: "", postcode: "", service: "", message: "" },
  });

  function onSubmit(values: z.infer<typeof formSchema>) {
    const subject = `Enquiry: ${values.service} - ${values.name}`;
    const body = `Name: ${values.name}%0D%0APhone: ${values.phone}%0D%0AEmail: ${values.email}%0D%0APostcode: ${values.postcode}%0D%0AService: ${values.service}%0D%0A%0D%0AMessage:%0D%0A${values.message || "No additional message."}`;
    window.location.href = `mailto:enquiries@dimensioncleaning.co.uk?subject=${subject}&body=${body}`;
    setIsSubmitted(true);
  }

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
    setMobileMenuOpen(false);
  };

  const services = [
    {
      title: "Driveway & Patio Pressure Washing",
      description: "Removes algae, moss, dirt and stubborn staining from block paving, tarmac and natural stone — restoring it to its original condition.",
      icon: <Droplets className="w-5 h-5" />,
    },
    {
      title: "Gutter Cleaning & Clearance",
      description: "Essential annual maintenance to prevent blockages, overflows and water damage to your property.",
      icon: <HomeIcon className="w-5 h-5" />,
    },
    {
      title: "Render & Exterior Wall Cleaning",
      description: "Specialist soft wash treatment that lifts algae, black spot and staining from rendered walls without damaging the surface.",
      icon: <ShieldCheck className="w-5 h-5" />,
    },
    {
      title: "Fascia, Soffit & uPVC Cleaning",
      description: "Restoring dirty, grey or green-tinged white plastic back to a look-new condition — inside and out.",
      icon: <ClipboardCheck className="w-5 h-5" />,
    },
    {
      title: "Window Cleaning",
      description: "Streak-free results on all windows and frames, keeping your home looking pristine year round.",
      icon: <CheckCircle2 className="w-5 h-5" />,
    },
  ];

  const results = [
    { label: "Drive Cleaning", image: beforeAfterDrive },
    { label: "Patio Cleaning", image: beforeAfterPatio },
    { label: "Render Cleaning", image: beforeAfterRender },
    { label: "Gutter Cleaning", image: beforeAfterGutter },
  ];

  return (
    <div className="min-h-screen bg-background text-foreground selection:bg-primary/30">

      {/* Navigation */}
      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          isScrolled
            ? "bg-background/95 backdrop-blur-md border-b border-border shadow-lg py-3"
            : "bg-transparent py-5"
        }`}
      >
        <div className="container mx-auto px-4 md:px-8 flex items-center justify-between">
          <a
            href="#"
            onClick={(e) => { e.preventDefault(); scrollTo("hero"); }}
            className="flex items-center"
            data-testid="link-logo"
          >
            <img src={logoSrc} alt="Dimension Exterior Cleaning" className="h-12 md:h-14 w-auto" />
          </a>

          <div className="hidden md:flex items-center gap-8">
            {["services", "results", "process", "why-us"].map((id) => (
              <button
                key={id}
                onClick={() => scrollTo(id)}
                className="text-sm font-semibold text-muted-foreground hover:text-foreground transition-colors capitalize tracking-wide"
                data-testid={`link-nav-${id}`}
              >
                {id === "why-us" ? "Why Us" : id === "process" ? "How It Works" : id.charAt(0).toUpperCase() + id.slice(1)}
              </button>
            ))}
            <Button
              onClick={() => scrollTo("contact")}
              className="rounded-full px-7 font-bold shadow-lg shadow-primary/20 hover:shadow-primary/40 transition-shadow"
              data-testid="button-get-quote-nav"
            >
              Get a Quote
            </Button>
          </div>

          <button
            className="md:hidden text-foreground p-1"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            data-testid="button-mobile-menu"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </nav>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="fixed inset-0 z-40 bg-background/98 backdrop-blur-md pt-24 px-6 flex flex-col gap-6 md:hidden">
          {[
            { id: "services", label: "Services" },
            { id: "results", label: "Our Results" },
            { id: "process", label: "How It Works" },
            { id: "why-us", label: "Why Us" },
          ].map(({ id, label }) => (
            <button
              key={id}
              onClick={() => scrollTo(id)}
              className="text-xl font-bold text-left text-foreground py-3 border-b border-border"
            >
              {label}
            </button>
          ))}
          <Button onClick={() => scrollTo("contact")} size="lg" className="w-full mt-4 text-base font-bold rounded-full">
            Get a Free Quote
          </Button>
        </div>
      )}

      {/* Hero */}
      <section id="hero" className="relative pt-32 pb-20 md:pt-44 md:pb-36 overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img
            src={brandBanner}
            alt="Dimension Exterior Cleaning — real results"
            className="w-full h-full object-cover object-center opacity-20"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-background via-background/85 to-background/30" />
          <div className="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent" />
        </div>

        <div className="container mx-auto px-4 md:px-8 relative z-10">
          <div className="max-w-3xl">
            <motion.div
              initial="hidden"
              animate="visible"
              variants={fadeUp}
              custom={0}
              className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-primary/15 border border-primary/30 text-primary text-sm font-semibold mb-8 tracking-wide"
            >
              <MapPin className="w-4 h-4" />
              South Yorkshire's Exterior Cleaning Specialists
            </motion.div>

            <motion.h1
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              custom={1}
              className="text-5xl md:text-7xl font-extrabold font-serif leading-[1.05] mb-6 text-white tracking-tight"
            >
              Bring your home's exterior{" "}
              <span className="text-primary">back to life.</span>
            </motion.h1>

            <motion.p
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              custom={2}
              className="text-lg md:text-xl text-muted-foreground mb-10 max-w-2xl leading-relaxed"
            >
              Professional driveway, patio, gutter and exterior cleaning across South Yorkshire.
              We turn up on time, do exceptional work, and leave your property immaculate. No mess — just results.
            </motion.p>

            <motion.div
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              custom={3}
              className="flex flex-col sm:flex-row gap-4"
            >
              <Button
                size="lg"
                onClick={() => scrollTo("contact")}
                className="text-base h-14 px-8 rounded-full shadow-xl shadow-primary/25 font-bold"
                data-testid="button-hero-quote"
              >
                Request Free Quote <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="text-base h-14 px-8 rounded-full border-border bg-card/50 backdrop-blur-sm hover:bg-card font-semibold"
                asChild
              >
                <a href="tel:01144573009" data-testid="link-hero-phone">
                  <PhoneCall className="mr-2 w-5 h-5" /> 0114 457 3009
                </a>
              </Button>
            </motion.div>

            <motion.div
              variants={fadeUp}
              initial="hidden"
              animate="visible"
              custom={4}
              className="mt-12 flex flex-wrap items-center gap-6 text-sm text-muted-foreground"
            >
              <span className="flex items-center gap-2"><CheckCircle2 className="w-5 h-5 text-primary" /> Vetted Professionals</span>
              <span className="flex items-center gap-2"><CheckCircle2 className="w-5 h-5 text-primary" /> Fully Insured</span>
              <span className="flex items-center gap-2"><CheckCircle2 className="w-5 h-5 text-primary" /> Free Condition Reports</span>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Trust Bar */}
      <div className="bg-card border-y border-border py-8">
        <div className="container mx-auto px-4 md:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            {[
              { stat: "100%", label: "Satisfaction Guaranteed" },
              { stat: "0", label: "Mess Left Behind" },
              { stat: "Free", label: "Condition Reports & Quotes" },
              { stat: "Local", label: "South Yorkshire Business" },
            ].map(({ stat, label }) => (
              <div key={label}>
                <p className="text-3xl font-extrabold font-serif text-primary mb-1">{stat}</p>
                <p className="text-sm text-muted-foreground">{label}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Services */}
      <section id="services" className="py-24 bg-background">
        <div className="container mx-auto px-4 md:px-8">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <p className="text-sm font-bold text-primary tracking-widest uppercase mb-3">Our Services</p>
            <h2 className="text-3xl md:text-5xl font-extrabold font-serif text-white mb-5">
              Everything your home exterior needs.
            </h2>
            <p className="text-muted-foreground text-lg">
              One call handles multiple exterior cleaning needs. Save time and deal with a tradesperson you can trust.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
            {services.map((service, idx) => (
              <motion.div
                key={idx}
                variants={fadeUp}
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                custom={idx * 0.5}
                className="group bg-card rounded-2xl p-6 border border-border hover:border-primary/40 transition-colors"
                data-testid={`card-service-${idx}`}
              >
                <div className="w-11 h-11 bg-primary/15 rounded-xl flex items-center justify-center text-primary mb-5">
                  {service.icon}
                </div>
                <h3 className="text-lg font-bold text-white mb-2 font-serif">{service.title}</h3>
                <p className="text-muted-foreground text-sm leading-relaxed mb-5">{service.description}</p>
                <button
                  onClick={() => scrollTo("contact")}
                  className="text-primary font-semibold text-sm flex items-center gap-1 group-hover:gap-2 transition-all"
                >
                  Get a quote <ChevronRight className="w-4 h-4" />
                </button>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Results — Before & After */}
      <section id="results" className="py-24 bg-card border-y border-border">
        <div className="container mx-auto px-4 md:px-8">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <p className="text-sm font-bold text-primary tracking-widest uppercase mb-3">Real Results</p>
            <h2 className="text-3xl md:text-5xl font-extrabold font-serif text-white mb-5">
              See the difference we make.
            </h2>
            <p className="text-muted-foreground text-lg">
              Every job is a before &amp; after transformation. These are real properties, real results — no filters.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 gap-6">
            {results.map(({ label, image }, idx) => (
              <motion.div
                key={idx}
                variants={fadeUp}
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                custom={idx * 0.5}
                className="rounded-2xl overflow-hidden border border-border shadow-xl"
                data-testid={`card-result-${idx}`}
              >
                <img
                  src={image}
                  alt={`${label} before and after`}
                  className="w-full h-auto object-cover"
                />
              </motion.div>
            ))}
          </div>

          <div className="text-center mt-12">
            <Button
              size="lg"
              onClick={() => scrollTo("contact")}
              className="rounded-full px-10 font-bold shadow-lg shadow-primary/20 text-base"
              data-testid="button-results-cta"
            >
              Book Your Transformation <ArrowRight className="ml-2 w-5 h-5" />
            </Button>
          </div>
        </div>
      </section>

      {/* How it Works */}
      <section id="process" className="py-24 bg-background">
        <div className="container mx-auto px-4 md:px-8">
          <div className="max-w-2xl mx-auto text-center mb-16">
            <p className="text-sm font-bold text-primary tracking-widest uppercase mb-3">The Process</p>
            <h2 className="text-3xl md:text-5xl font-extrabold font-serif text-white mb-5">
              Simple, reliable, transparent.
            </h2>
            <p className="text-muted-foreground text-lg">
              From the first call to the final rinse — here's exactly how we work.
            </p>
          </div>

          <div className="grid md:grid-cols-4 gap-6 relative">
            <div className="hidden md:block absolute top-10 left-[12.5%] right-[12.5%] h-px bg-gradient-to-r from-transparent via-primary/30 to-transparent z-0" />
            {[
              { n: "01", title: "Get in Touch", desc: "Fill out our enquiry form or give us a call. We'll discuss your needs and arrange a visit." },
              { n: "02", title: "Free Inspection & Quote", desc: "We assess your property and provide a fixed-price quote. No hidden fees, no surprises." },
              { n: "03", title: "We Do the Work", desc: "Our team arrives on time with professional equipment and completes the job to an exceptional standard." },
              { n: "04", title: "Zero Mess Guarantee", desc: "We rinse down adjacent areas, clear all debris and leave your property spotless." },
            ].map(({ n, title, desc }, idx) => (
              <motion.div
                key={n}
                variants={fadeUp}
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                custom={idx * 0.5}
                className="relative z-10 bg-card rounded-2xl border border-border p-7 text-center"
                data-testid={`card-step-${idx}`}
              >
                <div className="w-14 h-14 rounded-full bg-primary/15 border border-primary/30 flex items-center justify-center text-primary font-extrabold font-serif text-xl mx-auto mb-5">
                  {n}
                </div>
                <h3 className="text-lg font-bold font-serif text-white mb-3">{title}</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">{desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <section id="why-us" className="py-24 bg-card border-t border-border">
        <div className="container mx-auto px-4 md:px-8">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <p className="text-sm font-bold text-primary tracking-widest uppercase mb-3">Why Dimension</p>
            <h2 className="text-3xl md:text-5xl font-extrabold font-serif text-white mb-5">
              We don't cut corners.<br />We clean them.
            </h2>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                icon: <Clock className="w-7 h-7 text-primary" />,
                title: "We Respect Your Time",
                desc: "We keep you informed every step of the way. You'll always know when we're coming, and we'll never leave you hanging without a heads-up.",
              },
              {
                icon: <ShieldCheck className="w-7 h-7 text-primary" />,
                title: "Local & Accountable",
                desc: "As a South Yorkshire business, our reputation is everything. Every job has to be perfect — because word-of-mouth is our best marketing.",
              },
              {
                icon: <Star className="w-7 h-7 text-primary" />,
                title: "Proper Equipment",
                desc: "We use commercial-grade pressure washers, soft wash systems and specialist treatments — not the pressure washer from B&Q.",
              },
            ].map(({ icon, title, desc }, idx) => (
              <motion.div
                key={idx}
                variants={fadeUp}
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                custom={idx * 0.5}
                className="bg-background rounded-2xl p-8 border border-border"
                data-testid={`card-why-${idx}`}
              >
                <div className="w-14 h-14 bg-primary/10 rounded-2xl flex items-center justify-center mb-6">
                  {icon}
                </div>
                <h3 className="text-xl font-bold font-serif text-white mb-3">{title}</h3>
                <p className="text-muted-foreground leading-relaxed">{desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-24 bg-background border-t border-border">
        <div className="container mx-auto px-4 md:px-8">
          <div className="max-w-5xl mx-auto overflow-hidden rounded-3xl border border-border shadow-2xl flex flex-col md:flex-row">

            {/* Info Panel */}
            <div
              className="md:w-2/5 p-10 flex flex-col justify-between relative overflow-hidden"
              style={{ background: "linear-gradient(160deg, hsl(174 41% 32%), hsl(174 41% 20%))" }}
            >
              <div className="absolute inset-0 opacity-10"
                style={{ backgroundImage: "radial-gradient(circle at 80% 20%, white 0%, transparent 60%)" }}
              />
              <div className="relative z-10">
                <img src={logoSrc} alt="Dimension Exterior Cleaning" className="h-14 w-auto mb-8 brightness-0 invert" />
                <h3 className="text-3xl font-extrabold font-serif text-white mb-2">Get a Free Quote</h3>
                <p className="text-white/75 mb-10 text-sm leading-relaxed">
                  Fill out the form and we'll get back to you within 24 hours. Or call us direct — we're happy to talk.
                </p>

                <div className="space-y-6">
                  <a href="tel:01144573009" className="flex items-start gap-4 group" data-testid="link-contact-phone">
                    <PhoneCall className="w-5 h-5 text-white mt-0.5" />
                    <div>
                      <p className="font-bold text-white text-sm">Phone</p>
                      <p className="text-white/75 text-sm group-hover:text-white transition-colors">0114 457 3009</p>
                    </div>
                  </a>
                  <a href="https://wa.me/447494503865" target="_blank" rel="noopener noreferrer" className="flex items-start gap-4 group" data-testid="link-contact-whatsapp">
                    <svg className="w-5 h-5 text-white mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.124.554 4.12 1.526 5.854L0 24l6.316-1.508A11.955 11.955 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.896 0-3.67-.5-5.2-1.376l-.373-.222-3.867.923.967-3.776-.243-.389A9.937 9.937 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
                    <div>
                      <p className="font-bold text-white text-sm">WhatsApp / Text</p>
                      <p className="text-white/75 text-sm group-hover:text-white transition-colors">07494 503865</p>
                    </div>
                  </a>
                  <a href="mailto:enquiries@dimensioncleaning.co.uk" className="flex items-start gap-4 group" data-testid="link-contact-email">
                    <Mail className="w-5 h-5 text-white mt-0.5" />
                    <div>
                      <p className="font-bold text-white text-sm">Email</p>
                      <p className="text-white/75 text-sm group-hover:text-white transition-colors">enquiries@dimensioncleaning.co.uk</p>
                    </div>
                  </a>
                  <div className="flex items-start gap-4">
                    <MapPin className="w-5 h-5 text-white mt-0.5" />
                    <div>
                      <p className="font-bold text-white text-sm">Service Area</p>
                      <p className="text-white/75 text-sm">South Yorkshire &amp; Surrounding Areas</p>
                    </div>
                  </div>
                </div>
              </div>

              <div className="relative z-10 mt-10 pt-6 border-t border-white/20">
                <p className="text-white/60 text-xs">Dimension Cleaning is a trusted local business dedicated to domestic exterior maintenance.</p>
              </div>
            </div>

            {/* Form */}
            <div className="md:w-3/5 bg-card p-10">
              {isSubmitted ? (
                <div className="h-full flex flex-col items-center justify-center text-center py-12">
                  <div className="w-16 h-16 bg-primary/15 rounded-full flex items-center justify-center mb-6">
                    <CheckCircle2 className="w-8 h-8 text-primary" />
                  </div>
                  <h4 className="text-2xl font-bold font-serif text-white mb-2">Enquiry Sent!</h4>
                  <p className="text-muted-foreground max-w-xs">
                    Thanks for getting in touch. We'll review your details and come back to you shortly.
                  </p>
                  <Button variant="outline" className="mt-8 rounded-full" onClick={() => setIsSubmitted(false)}>
                    Send another enquiry
                  </Button>
                </div>
              ) : (
                <Form {...form}>
                  <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-5">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <FormField control={form.control} name="name" render={({ field }) => (
                        <FormItem>
                          <FormLabel>Full Name</FormLabel>
                          <FormControl>
                            <Input placeholder="John Smith" className="bg-background border-border" data-testid="input-name" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )} />
                      <FormField control={form.control} name="phone" render={({ field }) => (
                        <FormItem>
                          <FormLabel>Phone Number</FormLabel>
                          <FormControl>
                            <Input placeholder="07123 456789" className="bg-background border-border" data-testid="input-phone" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )} />
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <FormField control={form.control} name="email" render={({ field }) => (
                        <FormItem>
                          <FormLabel>Email Address</FormLabel>
                          <FormControl>
                            <Input type="email" placeholder="john@example.com" className="bg-background border-border" data-testid="input-email" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )} />
                      <FormField control={form.control} name="postcode" render={({ field }) => (
                        <FormItem>
                          <FormLabel>Postcode</FormLabel>
                          <FormControl>
                            <Input placeholder="S1 2AB" className="bg-background border-border" data-testid="input-postcode" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )} />
                    </div>

                    <FormField control={form.control} name="service" render={({ field }) => (
                      <FormItem>
                        <FormLabel>Service Required</FormLabel>
                        <Select onValueChange={field.onChange} defaultValue={field.value}>
                          <FormControl>
                            <SelectTrigger className="bg-background border-border" data-testid="select-service">
                              <SelectValue placeholder="Select a service" />
                            </SelectTrigger>
                          </FormControl>
                          <SelectContent>
                            <SelectItem value="Driveway & Patio">Driveway &amp; Patio Pressure Washing</SelectItem>
                            <SelectItem value="Gutter Cleaning">Gutter Cleaning &amp; Clearance</SelectItem>
                            <SelectItem value="Render & Exterior Wall">Render &amp; Exterior Wall Cleaning</SelectItem>
                            <SelectItem value="Fascia, Soffit & uPVC">Fascia, Soffit &amp; uPVC Cleaning</SelectItem>
                            <SelectItem value="Window Cleaning">Window Cleaning</SelectItem>
                            <SelectItem value="Roofline Inspection Report">Roofline Inspection Report</SelectItem>
                            <SelectItem value="Multiple Services">Multiple Services</SelectItem>
                            <SelectItem value="Other">Other</SelectItem>
                          </SelectContent>
                        </Select>
                        <FormMessage />
                      </FormItem>
                    )} />

                    <FormField control={form.control} name="message" render={({ field }) => (
                      <FormItem>
                        <FormLabel>Tell Us About Your Property <span className="text-muted-foreground font-normal">(optional)</span></FormLabel>
                        <FormControl>
                          <Textarea
                            placeholder="Size, access, specific problem areas..."
                            className="bg-background border-border resize-none"
                            rows={3}
                            data-testid="textarea-message"
                            {...field}
                          />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )} />

                    <Button
                      type="submit"
                      size="lg"
                      className="w-full rounded-full font-bold h-12 shadow-lg shadow-primary/20"
                      data-testid="button-submit"
                    >
                      Send Enquiry <ArrowRight className="ml-2 w-5 h-5" />
                    </Button>
                  </form>
                </Form>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-card border-t border-border py-10">
        <div className="container mx-auto px-4 md:px-8">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <img src={logoSrc} alt="Dimension Exterior Cleaning" className="h-10 w-auto" />
            <div className="text-center text-sm text-muted-foreground space-y-1">
              <p>
                <a href="tel:01144573009" className="hover:text-primary transition-colors">0114 457 3009</a>
                {" "}|{" "}
                <a href="https://wa.me/447494503865" className="hover:text-primary transition-colors" target="_blank" rel="noopener noreferrer">07494 503865 (WhatsApp/Text)</a>
                {" "}|{" "}
                <a href="mailto:enquiries@dimensioncleaning.co.uk" className="hover:text-primary transition-colors">enquiries@dimensioncleaning.co.uk</a>
              </p>
              <p>Service area: South Yorkshire and surrounding areas</p>
            </div>
            <p className="text-xs text-muted-foreground text-center md:text-right">
              &copy; {new Date().getFullYear()} Dimension Cleaning. All rights reserved.<br />
            </p>
          </div>
        </div>
      </footer>

    </div>
  );
}
