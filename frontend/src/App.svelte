<script>
  import Router from "svelte-spa-router";
  import routes from "./routes";

  import Counter from "./lib/Counter.svelte";
</script>

<main>
  <a href="/">Home</a>
  <a href="/#/about">About</a>
</main>

<Router {routes} />
