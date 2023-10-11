<script lang="ts">
    import { drawerStore } from '@skeletonlabs/skeleton';

function drawerClose(): void {
	drawerStore.close();
}
</script>

<nav class="list-nav p-4">
	<ul>
		<li><a href="/rio-online" on:click={drawerClose}>Homepage</a></li>
		<li><a href="/rio-online/tutorial" on:click={drawerClose}>Tutorial</a></li>
		<li><a href="/rio-online/events" on:click={drawerClose}>Events</a></li>
		<li><a href="/rio-online/optimize" on:click={drawerClose}>Optimize</a></li>
		<li><a href="/rio-online/version-history" on:click={drawerClose}>Version History</a></li>
	</ul>
</nav>