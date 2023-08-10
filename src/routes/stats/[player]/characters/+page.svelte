<script lang="ts">
    export let data;
    import { titleCase } from '$lib/utils';
  </script>
  
  {#if data}
  
    <section class="grid grid-cols-2 md:grid-cols-2 gap-4 h-screen">
      {#each Object.entries(data.data.Stats) as [key, value]}
        <div class="table-container">
            <div class="justify-center align-middle flex m-2">
            <h2 class="h2 text-token">{key}</h2>
            </div>
          <table class="table h-[80%] table-auto">
            {#each Object.entries(value) as [k, v]}

            <thead></thead>
            <tbody>
                <tr>
                  <td>{titleCase(k)}</td>
                  <!-- <td>{v}</td> -->
                  {#each Object.entries(v) as [ky, vl]}
                  <tr>
                    <td>{titleCase(ky)}</td>
                    <td>{vl}</td>
                  </tr>
                {/each}
                </tr>
            </tbody>
            {/each}
          </table>
        </div>
      {/each}
    </section>
  {/if}
  