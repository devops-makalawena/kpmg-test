package main

import (
	"fmt"
	"strings"
)

func main() {
	object1 := map[string]interface{}{
		"a": map[string]interface{}{
			"b": map[string]interface{}{
				"c": "d",
			},
		},
	}

	object2 := map[string]interface{}{
		"x": map[string]interface{}{
			"y": map[string]interface{}{
				"z": "a",
			},
		},
	}

	key1 := "a.b.c"
	key2 := "x.y.z"

	value1, err1 := GetNestedValue(object1, key1)
	value2, err2 := GetNestedValue(object2, key2)

	if err1 != nil {
		fmt.Println("Error:", err1)
	} else {
		fmt.Println("Value 1:", value1)
	}

	if err2 != nil {
		fmt.Println("Error:", err2)
	} else {
		fmt.Println("Value 2:", value2)
	}
}

// GetNestedValue retrieves a value from a nested object using a key of any format
func GetNestedValue(obj interface{}, key string) (interface{}, error) {
	keys := strings.Split(key, ".")

	for _, k := range keys {
		if m, ok := obj.(map[string]interface{}); ok {
			val, found := m[k]
			if !found {
				return nil, fmt.Errorf("Key '%s' not found", k)
			}
			obj = val
		} else {
			return nil, fmt.Errorf("Invalid object type at key '%s'", k)
		}
	}

	return obj, nil
}
