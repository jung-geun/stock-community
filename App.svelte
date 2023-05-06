<script>
  async function hello(url=""){
    const _url = "http://127.0.0.1:8000/" + url;
    const res = await fetch(_url);
    const json = await res.json();
    if (res.ok) {
      return json.message;
    } else {
      throw new Error(json.message);
    }
  }

  let promise = hello("svelte");
</script>

{#await promise}
  <p>...waiting</p>
{:then message}
  {#if message}
    <h1>{message}</h1>
  {:else}
    <h1>no message</h1>
  {/if}
{/await}
