import Home from "./pages/Home.svelte";
import About from "./pages/About.svelte";
import Game from "./pages/game/index.svelte";
import GameDetail from "./pages/game/[id].svelte";
import NotFound from "./pages/NotFound.svelte";

export default {
  "/": Home,
  "/about": About,
  "/game": Game,
  "/game/:id": GameDetail,
  "*": NotFound,
};
