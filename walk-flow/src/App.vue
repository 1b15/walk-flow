<template>
	<div id="app">
		<h1 style="text-align: center">WalkFlow: Analyzing pedestrian volumes</h1>
		<div class="container">
			<div class="row main">
				<label for="usageTypesSelector">Why are people walking there?</label>
				<b-form-select id="usageTypesSelector" v-model="usage" :options="usageTypes"></b-form-select>
			</div>
			<div class="row main" v-for="(measure, index) in measures">
				<h5 class="col-auto" style="white-space: nowrap;">Measure {{index+1}}</h5>
				<div class="col">
					<div class="row mb-1">
						<div class="col">
							<label>What day did you count?</label>
						</div>
						<div class="col-md-4">
							<b-form-input v-model="measure.date" type="date"></b-form-input>
						</div>
					</div>
					<div class="row mb-1">
						<div class="col">
							<label>How many people did you count?</label>
						</div>
						<div class="col-md-4">
							<b-form-input v-model="measure.counted" type="number"></b-form-input>
						</div>
					</div>
					<div class="row mb-1">
						<div class="col">
							<label>What was the temperature like when you counted?</label>
						</div>
						<div class="col-md-4">
							<div class="input-group">
								<b-form-input v-model="measure.temperature" type="number"></b-form-input>
								<div class="input-group-append">
									<span class="input-group-text">°C</span>
								</div>
							</div>
						</div>
					</div>
					<div class="row mb-1">
						<div class="col">
							<label>How much rain did fall when you counted?</label>
						</div>
						<div class="col-md-4">
							<div class="input-group">
								<b-form-input v-model="measure.rain" type="number"></b-form-input>
								<div class="input-group-append">
									<span class="input-group-text">mm</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="row main">
				<button type="button" class="btn btn-primary" @click="addMeasure">Add another counting</button>
			</div>
			<div class="alert alert-success" role="alert" v-if="projection">
				<h5>Projection calculated</h5>
				<table class="table table-bordered">
					<tr>
						<th>Average daily traffic</th>
						<td>{{projection.day}}</td>
					</tr>
					<tr>
						<th>Average weekdaily traffic</th>
						<td>{{projection.weekday}}</td>
					</tr>
					<tr>
						<th>Expected yearly traffic</th>
						<td>{{365*projection.day}}</td>
					</tr>
				</table>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'app',
		data() {
			return {
				usage: null,
				usageTypes: [
					{value: null, text: 'unknown'},
					{value: 'work', text: 'Work'},
					{value: 'education', text: 'Education'},
					{value: 'shopping', text: 'Shopping'},
					{value: 'leisure', text: 'Leisure'},
				],
				measures: [{}],
				projection: null
			}
		},
		computed: {
			getRequestData: function () {
				return {
					usage: this.usage,
					measures: this.measures
				}
			},
			getRequestDataString: function () {
				return JSON.stringify(this.getRequestData)
			},
			isRequestDataValid: function () {
				for (const measure of this.measures) {
					if (!measure.date) {
						return false
					}
					if (!measure.counted) {
						return false
					}
				}
				return true
			}
		},
		watch: {
			getRequestDataString: function (newRequestData) {
				this.projection = null
				if (this.isRequestDataValid) {
					axios.get('http://localhost:8000/predict', this.getRequestData).then((response) => {
						this.projection = response.data
					})
				}
			}
		},
		methods: {
			addMeasure() {
				this.measures.push({})
			}
		}
	}
</script>

<style>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		color: #2c3e50;
		margin-top: 60px;
	}

	.row.main {
		margin-top: 1em;
		margin-bottom: 1em;
	}
</style>
