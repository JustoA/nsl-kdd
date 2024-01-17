import pandas as pd
import matplotlib.pyplot as plt


# Function to load NSL-KDD dataset from CSV
def load_nsl_kdd_dataset(file_path):
    # Define column names based on the dataset description
    column_names = [
        "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
        "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
        "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
        "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
        "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
        "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
        "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
        "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "attack_type", "label"
    ]

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=None, names=column_names)

    return df


# Function to plot a bar chart of attack types
def plot_attack_distribution(dataset, name):

    # Load the dataset
    df = load_nsl_kdd_dataset(dataset)

    # Group by attack type and count occurrences
    attack_distribution = df['attack_type'].value_counts()

    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    attack_distribution.plot(kind='bar', color='skyblue')
    plt.title(f'Distribution of Attack Types in NSL-KDD {name} Dataset')
    plt.xlabel('Attack Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()




# Plot the distribution of attack types
plot_attack_distribution(r'NSL-KDD/KDDTrain+.txt', 'Train')
plot_attack_distribution(r'NSL-KDD/KDDTest+.txt', 'Test')
