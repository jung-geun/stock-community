<script>
  import Router from "svelte-spa-router";
  import routes from "./routes.js";
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";
  import Counter from "./lib/Counter.svelte";
</script>

<Header />

<main />

<Router {routes} />

<Footer />
