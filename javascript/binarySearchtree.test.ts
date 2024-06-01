const {describe, expect, test} = require('@jest/globals');
const { BinaryNode, BinarySearchTree } = require('./binarySearchTree');

describe('binary search tree insert', () => {
  test('if tree is empty inserted node becomes root', () => {
    const testTree = new BinarySearchTree()
    const testNumber = 40
    testTree.insert(testNumber)
    expect(testTree.root.data).toBe(40);
  });
  test('insert bigger than 40 is inserted to the right', () => {
    const testTree = new BinarySearchTree()
    const testNumber1 = 40
    const testNumber2 = 45
    testTree.insert(testNumber1)
    testTree.insert(testNumber2)
    expect(testTree.root.right.data).toBe(45);
  });
});

describe('search function', () => {
  test('search functions returns Binary Node if number in tree', () => {
    const testTree = new BinarySearchTree()
    for (let item of [30, 40, 23, 100, -1, 33]) {
      testTree.insert(item);
    }
    const searchResult = testTree.search(23)

    expect(searchResult.data).toBe(23);
  });
});