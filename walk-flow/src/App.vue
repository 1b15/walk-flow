<template>
	<div id="app">
		<h1 style="text-align: center">WalkFlow: Analyzing pedestrian volumes</h1>
		<div class="container">
			<div class="row main">
				<label>Where did you count?</label>
				<b-form-select v-model="countingPoint" :options="countingPoints"></b-form-select>
			</div>
			<div class="row main">
				<label>When did you count?</label>
				<b-form-select v-model="dow" :options="dows"></b-form-select>
			</div>
			<div class="row main" v-if="false">
				<label for="usageTypesSelector">Why are people walking there?</label>
				<b-form-select id="usageTypesSelector" v-model="usage" :options="usageTypes"></b-form-select>
			</div>
			<div class="row main" v-for="(measure, index) in measures" v-if="false">
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
			<div class="row main" v-if="false">
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
				countingPoint: null,
				countingPoints: [
					{value: null, text: 'unknown'},
					{value: '809 Allschwilerstrasse 77/86', text: 'Allschwilerstrasse 77/86'},
					{value: '903 Äussere Baselstrasse 328', text: 'Äussere Baselstrasse 328'},
					{value: '911 Birskopfsteg', text: 'Birskopfsteg'},
					{value: '913 Burgfelderstrasse', text: 'Burgfelderstrasse'},
					{value: '405 Dorenbachviadukt', text: 'Dorenbachviadukt'},
					{value: '350 Dreirosenbrücke', text: 'Dreirosenbrücke'},
					{value: '817 Elisabethenanlage', text: 'Elisabethenanlage'},
					{value: '814 Elisabethenstrasse 46*', text: 'Elisabethenstrasse 46'},
					{value: '918 Elsässerrheinweg', text: 'Elsässerrheinweg'},
					{value: '912 Elsässerstrasse 261/260', text: 'Elsässerstrasse 261/260'},
					{value: '660 Flughafenstrasse', text: 'Flughafenstrasse'},
					{value: '909 General Guisan-Strasse 104', text: 'General Guisan-Strasse 104'},
					{value: '806 Gerbergasse', text: 'Gerbergasse'},
					{value: '908 Grenzacherstrasse (Kraftwerk)', text: 'Grenzacherstrasse (Kraftwerk)'},
					{value: '807 Güterstrasse 180/183', text: 'Güterstrasse 180/183'},
					{value: '904 Hammerstrasse 90', text: 'Hammerstrasse 90'},
					{value: '813 Hardstrasse 66/77', text: 'Hardstrasse 66/77'},
					{value: '906 Hegenheimerstrasse 44', text: 'Hegenheimerstrasse 44'},
					{value: '403 Heuwaage-Viadukt', text: 'Heuwaage-Viadukt'},
					{value: '914 Hiltalingerstrasse', text: 'Hiltalingerstrasse'},
					{value: '920 J. Burckhardt-Strasse', text: 'J. Burckhardt-Strasse'},
					{value: '803 Johanniterbrücke', text: 'Johanniterbrücke'},
					{value: '352 Johanniterbrücke', text: 'Johanniterbrücke'},
					{value: '802 Klybeckstrasse 113/Kirche', text: 'Klybeckstrasse 113/Kirche'},
					{value: '905 Leimenstrasse 4', text: 'Leimenstrasse 4'},
					{value: '915 Luzernerring-Brücke', text: 'Luzernerring-Brücke'},
					{value: '815 Mittlere Rheinbrücke', text: 'Mittlere Rheinbrücke'},
					{value: '811 Mülhauserstrasse 110/122', text: 'Mülhauserstrasse 110/122'},
					{value: '810 Neubadstrasse 124/137', text: 'Neubadstrasse 124/137'},
					{value: '901 Peter-Merian Weg', text: 'Peter-Merian Weg'},
					{value: '805 Rebgasse 11/28', text: 'Rebgasse 11/28'},
					{value: '804 Rosentalstrasse 29/28', text: 'Rosentalstrasse 29/28'},
					{value: '659 Schlachthofstrasse', text: 'Schlachthofstrasse'},
					{value: '816 Schmiedgasse 4/7 (Riehen)', text: 'Schmiedgasse 4/7 (Riehen)'},
					{value: '917 Schwarzwaldbrücke', text: 'Schwarzwaldbrücke'},
					{value: '919 St. Alban-Rheinweg', text: 'St. Alban-Rheinweg'},
					{value: '910 St. Galler-Ring 101', text: 'St. Galler-Ring 101'},
					{value: '916 Stückisteg', text: 'Stückisteg'},
					{value: '902 Viaduktstrasse', text: 'Viaduktstrasse'},
					{value: '907 Wasgenring 62', text: 'Wasgenring 62'},
					{value: '354 Wettsteinbrücke', text: 'Wettsteinbrücke'},
					{value: '812 Wettsteinbrücke', text: 'Wettsteinbrücke'},
					{value: '808 Wolfschlucht-Promenade', text: 'Wolfschlucht-Promenade'}
				],
				dow: 6,
				dows: [
					{value: 0, text: 'Monday'},
					{value: 1, text: 'Tuesday'},
					{value: 2, text: 'Wednesday'},
					{value: 3, text: 'Thursday'},
					{value: 4, text: 'Friday'},
					{value: 5, text: 'Saturday'},
					{value: 6, text: 'Sunday'},
				],
				measures: [{}],
				projection: null
			}
		},
		computed: {
			getRequestData: function () {
				return {
					countingPoint: this.countingPoint,
					dow: this.dow
				}
			},
			getRequestDataString: function () {
				return JSON.stringify(this.getRequestData)
			},
			isRequestDataValid: function () {
				return this.countingPoint!=null
				// for (const measure of this.measures) {
				// 	if (!measure.date) {
				// 		return false
				// 	}
				// 	if (!measure.counted) {
				// 		return false
				// 	}
				// }
				// return true
			}
		},
		watch: {
			getRequestDataString: function (newRequestData) {
				this.projection = null
				if (this.isRequestDataValid) {
					axios.post('http://localhost:8000/predict', this.getRequestData).then((response) => {
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
