var
	sinon = require("sinon"),
	Tree = require('..').Tree
;

module.exports = {

	setUp: function(done) {
		this.tree = new Tree();
		done();
	},

	'should initialize with empty root': function(test) {
		test.equal(this.tree.root, null);
		test.done();
	},

	'should insert root node': function(test) {
		var node = this.tree.insert(10, 'ten');

		test.equal(node, this.tree.root);
		test.equal(node.key, 10);
		test.equal(node.value, 'ten');
		test.done();
	},

	'should stringify data': function(test) {
		this.tree.insert(10, 'ten');
		this.tree.insert(5, 'five');
		this.tree.insert(15, 'fifteen');

		test.equal(
			this.tree.stringify(),
			'{' +
				'"key":10,'+
				'"value":"ten",' +
				'"left":{' +
					'"key":5,' +
					'"value":"five",' +
					'"left":null,' +
					'"right":null' +
				'},' +
				'"right":{' +
					'"key":15,' +
					'"value":"fifteen",'+
					'"left":null,' +
					'"right":null' +
				'}' +
			'}'
		);
		test.done();
	},

	'should parse json': function(test) {
		var
			data = {
				key: 4,
				value: 'd',
				left: {
					key: 2,
					value: 'b',
					left: {
						key: 1,
						value: 'a',
						left: null,
						right: null
					},
					right: {
						key: 3,
						value: 'c',
						left: null,
						right: null
					}
				},
				right:{
					key: 5,
					value: 'e',
					left: null,
					right: {
						key: 6,
						value: 'f',
						left: null,
						right: null
					}
				}
			},
			json = JSON.stringify(data)
		;

		this.tree.parse(json);
		test.equal(this.tree.stringify(), json);
		test.done();
	}
};
