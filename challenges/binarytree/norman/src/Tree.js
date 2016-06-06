var
	Node = require('./Node')
;


module.exports = Tree;

function Tree() {
	this.root = null;
}

Tree.prototype.insert = function(key, value) {
	if (this.root) {
		return this.root.insert(key, value);
	} else {
		return (this.root = new Node(key, value));
	}
};

Tree.prototype.find = function(key) {
	return this.root ? this.root.find(key) : undefined;
};

Tree.prototype.parse = function(str) {
	this.root = (function(data, parent) {
		if (!data) {
			return null;
		}

		var node = new Node(
			parseInt(data.key, 10),
			data.value,
			parent
		);
		node.left = arguments.callee(data.left, node);
		node.right = arguments.callee(data.right, node);

		return node;
	})(JSON.parse(str), null);
};

Tree.prototype.stringify = function() {
	var data = this.root ? this.root.toObject() : {};
	return JSON.stringify(data);
};
