<script lang="ts">
    import { stadiums } from '$lib/helpers/stadiumName';
    import { getAllTagSets } from '$lib/helpers/tagNames';
    export let data;
    import { tagsets } from '$lib/stores/tagsets';
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    // Access the tagsets data in your component
let tagsetsData: any[] = []
$: {
tagsetsData = $tagsets; // Get the current value of the tagsets store
}

onMount(() => {
    getAllTagSets();
})
</script>


<!-- recent games table (diff page..?) -->
{#if data.games}
<h2 style="display:flex;justify-content:center;align-items:center;">{$page.params.player}</h2>
<table>
  <thead>
      <tr>
          <th>Away Player</th>
          <th>Away Score</th>
          <th>Home Score</th>
          <th>Home Player</th>
          <th>Stadium</th>
          <th>Game Mode</th>
          <th>Time</th>
      </tr>
  </thead>
  <tbody>
      {#each data.games as games}
              <tr>
                <td class="player-link"><a class="player" href={`/slice/player/${games.away_user}`}>{games.away_user}</a></td>
                <td>{games.away_score}</td>
                  <td>{games.home_score}</td>
                  <td class="player-link"><a class="player" href={`/slice/player/${games.home_user}`}>{games.home_user}</a></td>
                  <td>{stadiums[games.stadium]}</td>
                  <td class="mode"><a href={`/slice/${tagsetsData.find(tagset => tagset.id === games.game_mode)?.name}`}/ladder>{tagsetsData.find(tagset => tagset.id === games.game_mode)?.name || ''}</a></td>

                  <td>{new Date(games.date_time_start * 1000).toLocaleString()}</td>
              </tr>
      {/each}
  </tbody>
</table>
{/if}