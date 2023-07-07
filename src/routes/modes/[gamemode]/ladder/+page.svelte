<script lang="ts">
    // Import store
    import { page } from '$app/stores';
	import { BACKEND, UNCATEGORIZED_ENDPOINTS } from '$lib/constants';

    // right now this isn't working ...?
    import { sortableTableAction } from 'svelte-legos';
    // Import components

    
    // Instantiate variables
    let players: any = [];
  
    // Call on page load
    getTagSetLadder();
    async function getTagSetLadder() {
      try {
        const response = await fetch(BACKEND + UNCATEGORIZED_ENDPOINTS.GET_TAG_SET, {
          method: "POST",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            "TagSet": $page.params.gamemode
          })
        });
        const result = await response.json();
        // console.log(result);
        players = Object.values(result).sort((a: any, b: any) => b.rating - a.rating);
      } catch (error) {
        console.log(error);
      }
    }
  
  </script>

  <a href="/modes"><button class="game-mode">Return to Games List</button></a>

  
  <h1>{$page.params.gamemode}</h1>
  <section class="table-container">
    <table class="table" use:sortableTableAction>
      <thead>
      <tr>
        <th>#</th>
        <th>Glicko Rating</th>
        <th>Username</th>
        <th>W/L/T</th>
      </tr>
      </thead>
      <tbody>
      {#if players}
        {#each players as player, i}
          <tr>
            <td>{i + 1}</td>
            <td>{player.rating}</td>
            <td class="player-link"><a class="player" href={`/modes/player/${player.username}`}>{player.username}</a></td>
            <td>{player.num_wins}/{player.num_losses}/{player.num_ties}</td>
          </tr>
        {/each}
      {/if}
      <tr></tr>
    </tbody>
    </table>
  </section>