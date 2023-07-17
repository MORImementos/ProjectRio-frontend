<script lang="ts">
    // Import store
    import { page } from '$app/stores';
	import { BACKEND, UNCATEGORIZED_ENDPOINTS } from '$lib/constants';
  import { titleCase } from '$lib/utils';
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

  <!-- <a href="/modes"><button class="game-mode">Return to Games List</button></a> -->
  <div class="flex-auto">
  <a href={`/modes/` + $page.params.gamemode + `/peak`}><input type="checkbox" id="peak" name="peak">
    <label for="peak">View player peaks for this Game Mode.</label></a>
  </div>
  <h1>{titleCase($page.params.gamemode)}</h1>
  <section class="table-container">
    <table class="table table-hover table-interactive" use:sortableTableAction>
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
          <tr class="">
            <td>{i + 1}</td>
            <td>{player.rating}</td>
            <td class="player-link "><a class="player decoration-transparent" href={`/modes/player/${player.username}`}>{player.username}</a></td>
            <td>{player.num_wins}/{player.num_losses}/{player.num_ties}</td>
          </tr>
        {/each}
      {/if}
    </tbody>
    </table>
  </section>

  <style>
    td a {
      color: rgba(var(--text-neutral-500) / 1) !important; 
    }
  </style>
