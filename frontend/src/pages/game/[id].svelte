<script>
  import { params } from "svelte-spa-router";
  // import "../../lib/api";
</script>

{$params.id}
<!-- {if $params.id === "rock-scissors-paper"} -->
{#if $params.id == "rock-scissors-paper"}
  <h1>가위바위보</h1>
  <input type="number" name="inputs" />
{/if}
