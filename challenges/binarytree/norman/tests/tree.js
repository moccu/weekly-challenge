var
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

	'should parse json': function(test) {
		var
			json = '{"key":"4","value":"d","left":{"key":"2","value":"b","left":{"key":"1","value":"a","left":null,"right":null},"right":{"key":"3","value":"c","left":null,"right":null}},"right":{"key":"5","value":"e","left":null,"right":{"key":"6","value":"f","left":null,"right":null}}}'
		;

		this.tree.parse(json);
		test.ok(true);
		test.done();
	}
};
